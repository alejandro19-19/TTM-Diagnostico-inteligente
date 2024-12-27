from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from aplicacion_tesis.settings import secretos
from sklearn.tree import DecisionTreeClassifier as arboles
from sklearn.neural_network import MLPClassifier as redes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from .procesar_datos.convertir_datos import convertir_datos
from .forms.forms import FormularioUsuario, DatosDiagnostico
from .modelos_config import configuracion
from .modelos_config.configuracion import obtener_parametros_modelo as parametros
from .modelos_config.entrenar_modelo import busqueda_aleatoria
from .modelos_config.entrenar_modelo import busqueda_exhaustiva
import joblib 
import os
import pandas as pd
import random
import string
import smtplib
import json
import requests
import googleapiclient

"""

Apartado para cargar los modelos y el pipeline

"""

def cargar_modelo(auxiliar_ruta_modelo):
  auxiliar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  ruta_modelo = os.path.join(auxiliar, "modelos", auxiliar_ruta_modelo)
  
  if os.path.exists(ruta_modelo): # verificar si existe el archivo
    modelo = joblib.load(ruta_modelo)
    return modelo
  else:
    raise FileNotFoundError(f"El modelo {auxiliar_ruta_modelo} no se encuentra en la ruta especificada: {ruta_modelo}")

def cargar_modelos():
  # Cargar los modelos de IA
  modelos = [cargar_modelo(nombre) for nombre in configuracion.nombres_modelos]
  return modelos

def crear_modelos(modelo):
  # Crear nuevos modelos para el reentrenamiento
  modelos = []
  cantidad_modelos = len(configuracion.nombres_modelos)

  # Dependiendo del tipo de modelo se crea modelos de redes neuronales o de arboles de decision
  if modelo == "arboles":
    modelos = [arboles(random_state=123) for _ in range(cantidad_modelos)]
  elif modelo == "redes":
    modelos = [redes() for _ in range(cantidad_modelos)]

  return modelos

def cargar_pipeline():
  #Cargar el pipeline necesario para los modelos
  auxiliar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  ruta_pipeline = os.path.join(auxiliar, "modelos", "pipeline_model.pkl")
  
  if os.path.exists(ruta_pipeline): # verificar si existe el archivo
    pipeline = joblib.load(ruta_pipeline)
    return pipeline
  else:
    raise FileNotFoundError(f"El archivo pipeline_model.pkl no se encuentra en la ruta especificada: {ruta_pipeline}")

"""

Diagnosticar con los modelos

"""

def predecir_modelos(modelos,datos_con_pipeline):
  #Genera las probabilidades que asigna los modelos a los datos ingresados mediante el formulario
  predicciones = []
  for modelo in modelos:
    predicciones.append(modelo.predict_proba(datos_con_pipeline))
  return predicciones

"""

Funcion auxiliar para unir los datos ingresados y los datos actuales

"""

def unir_datos(datos_viejos, datos_nuevos):
  datos_combinados = pd.concat([datos_viejos, datos_nuevos], ignore_index=True)
  return datos_combinados

"""

Login para el usuario

"""

def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user:
      if user.is_active:
        # El usuario consiguio ingresar a su cuenta.
        login(request,user)
        return HttpResponseRedirect(reverse('index'))
      else:
        # El usuario no tiene una cuenta activa:
        return render(request,'error.html',{
          'error': 'La cuenta está desactivada.'
        })
    else:
      return render(request,'error.html',{
        'error': 'Usuario o contraseña incorrectos.'
        })
  else:
    return render(request, 'iniciar_sesion.html', {})

"""

Registrarse en la aplicacion

"""

def register(request):
  registered = False

  if request.method == 'POST':
    user_form = FormularioUsuario(data=request.POST)

    # Verificar si el usuario ingreso correctamente la informacion
    if user_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()
      registered = True
    else:
      return render(request,'error.html',{
        'error': user_form.errors
      })
  else:
    user_form = FormularioUsuario()
  
  return render(request,'registrarse.html',{
    'user_form':user_form,
    'registered': registered
  })

"""

Reentrenamiento del modelo utilizando la tecnica empleada

"""

def entrenar_modelo(modelo, x, y, nombre):
  tipo_modelo = configuracion.tipo_modelo
  param_grid = parametros(tipo_modelo)

  if tipo_modelo == "redes":
    # Utilizando redes neuronales

    # Busqueda del modelo con los mejores hiperparametros usando RandomSearch
    random_search_dt = busqueda_aleatoria(modelo, param_grid)
    random_search_dt.fit(x, y)

    best_score = random_search_dt.best_score_
    mejor_dt = random_search_dt.best_estimator_
    puntuacion = best_score
    joblib.dump(mejor_dt, 'modelos/'+'modelo'+'_'+nombre+'.pkl')
  
  elif tipo_modelo == "arboles":
    # Utilizando árboles de decisión
    # Búsqueda del modelo con los mejores hiperparámetros usando GridSearchCV
    grid_search_dt = busqueda_exhaustiva(modelo, param_grid)
    grid_search_dt.fit(x, y)

    best_score = grid_search_dt.best_score_
    mejor_dt = grid_search_dt.best_estimator_
    puntuacion = best_score
    joblib.dump(mejor_dt, 'modelos/'+'modelo'+'_'+nombre+'.pkl')

  else:
    raise ValueError("Tipo de modelo no soportado")

  return puntuacion

"""

Reentrenar todos los modelos

"""

def reentrenar_modelos(modelos, datos_x, datos_y):
  puntajes = []
  nombres_modelos = ['mialgia', 'dMiofacial', 'artralgiaI', 'artralgiaD', 'cReduccionI', 'cReduccionD']
    
  try:
    for i, nombre in enumerate(nombres_modelos):
      puntajes.append(entrenar_modelo(modelos[i], datos_x, datos_y[nombre], nombre))
    return 1, puntajes
  except Exception as e:
    return str(e)
  
"""

Funcion auxiliar para generar una contraseña aleatoria

"""
  
def generar_contrasena_temporal():
  caracteres = string.ascii_letters + string.digits
  return ''.join(random.choice(caracteres) for _ in range(20))

"""

Funcion para enviar la contraseña generada al correo registrado en la aplicacion

"""

def enviar_contrasena_email(email, contrasena_temporal):
  s = smtplib.SMTP(host='smtp.gmail.com', port=587)
  s.starttls()
  s.login(secretos["EMAIL"], secretos["PASSWORD"])

  msg = MIMEMultipart()
  msg['From'] = secretos["EMAIL"]
  msg['To'] = email
  msg['Subject'] = "Solicitud Recuperacion de Contraseña" 
  
  message = f'Su contraseña temporal es: {contrasena_temporal}\nInicie sesión y cambie su contraseña inmediatamente.'
  msg.attach(MIMEText(message, 'plain'))

  s.send_message(msg)
  del msg   
  s.quit()

"""

Solicitar un cambio de contraseña (se envia la nueva contraseña al correo)

"""

def solicitud_cambiar_contrasena(request):
  if request.method == 'POST':
    email = request.POST['email']
    try:
      usuario = User.objects.get(email=email)
    except User.DoesNotExist:
      return render(request,'error.html',{
        'error':'No existe una cuenta registrada con este correo.'
      })
    contrasena_temporal = generar_contrasena_temporal()
    usuario.set_password(contrasena_temporal)
    usuario.save()

    enviar_contrasena_email(email, contrasena_temporal)

    return render(request,'acierto.html',{
      'informacion':"Se ha enviado una contraseña temporal a su correo."
    })

  return render(request, 'recuperar_contrasena.html')

"""

Cambiar la contraseña pero con la cuenta logueada

"""

@login_required
def cambiar_contrasena(request):
  if request.method == 'POST':
    contrasena_actual = request.POST['current_password']
    nueva_contrasena = request.POST['new_password']
    confirmar_contrasena = request.POST['confirm_password']

    usuario = request.user
    if usuario.check_password(contrasena_actual):
      if nueva_contrasena == confirmar_contrasena:
        usuario.set_password(nueva_contrasena)
        usuario.save()
        logout(request)
        return render(request,'acierto.html',{
          'informacion':"Su contraseña ha sido cambiada exitosamente."
        })
      else:
        return render(request,'error.html',{
          'error':'Las nuevas contraseñas no coinciden.'
        })
    else:
      return render(request,'error.html',{
        'error':'La contraseña actual no es correcta.'
      })

  return render(request, 'cambiar_contrasena.html')

"""

Funcion para realizar el diagnostico de los datos ingresados en la aplicacion

"""

def predecir(request):
  if request.method == 'POST':
    datos = DatosDiagnostico(request.POST)
    if datos.is_valid():
      datos_procesados = convertir_datos(datos)
      columnas = configuracion.columnas
      datos_procesados = [datos_procesados]
      datos_entrada_df = pd.DataFrame(datos_procesados, columns=columnas)

      modelos = cargar_modelos()
      pipeline = cargar_pipeline()
      datos_con_pipeline = pipeline.transform(datos_entrada_df)
      predicciones = predecir_modelos(modelos,datos_con_pipeline)

      datos_json = json.dumps(datos_procesados[0])

      return render(request,'diagnostico.html',{
        'mialgia' : int(predicciones[0][0][1]*100),
        'dMiofacial' : int(predicciones[1][0][1]*100),
        'artralgiaI' : int(predicciones[2][0][1]*100),
        'artralgiaD' : int(predicciones[3][0][1]*100),
        'cReduccionI' : int(predicciones[4][0][1]*100),
        'cReduccionD' : int(predicciones[5][0][1]*100),
        'datos_json': datos_json
      })
    else:
      return render(request,'error.html',{
        'error': 'El formulario se ha ingresado de forma incorrecta.'
        })

  return render(request, 'formulario_prediccion.html')

"""

Funcion para integrar el diagnostico final del usuario en los datos actuales

"""

def integrar_diagnostico_medico(request):
  if request.method == 'POST':
    datos_con_pipeline = json.loads(request.POST['datos_con_pipeline'])

    diagnosticos = auxiliar_integrar_diagnostico(request)
    datos_guardar = datos_con_pipeline + diagnosticos
    guardar_datos = post_datos(datos_guardar)
    if guardar_datos == False:
      return render(request,'error.html',{
        'error':'No se han podido guardar los datos correctamente.'
      })
    return render(request,'acierto.html',{
      'informacion':"Se guardó exitosamente el diagnóstico ingresado",
    })
  
"""

Funcion auxiliar para corregir el diagnostico realizado por los modelos

"""

def auxiliar_integrar_diagnostico(request):
  diagnosticos = [0] * 17

  parametros = [
    ("mialgia", "mialgia_opcion", -17),
    ("dMiofacial", "dMiofacial_opcion", -16),
    ("artralgiaI", "artralgiaI_opcion", -15),
    ("artralgiaD", "artralgiaD_opcion", -14),
    ("cReduccionI", "cReduccionI_opcion", -12),
    ("cReduccionD", "cReduccionD_opcion", -11),
  ]

  for valor_key, opcion_key, index in parametros:
    valor = int(request.POST.get(valor_key))
    opcion = request.POST.get(opcion_key)

    if opcion == "no":
      diagnosticos[index] = 1 if valor < 50 else 0
    else:
      diagnosticos[index] = 0 if valor < 50 else 1

  return diagnosticos

"""

Funcion para reentrenar los modelos, ingresando un excel con datos nuevos, o con los datos actuales

"""

def reentrenar(request):
  if request.method == 'POST':
    try:
      archivo_excel = request.FILES['archivo_excel']
      datos_nuevos = pd.read_excel(archivo_excel)
    except Exception as e:
      pass

    try:   
      datos_viejos = get_datos()
    except:
      return render(request,'error.html',{
        'error':'Se presentó un problema con los datos previos del modelo.'
      })
    try:
      datos = unir_datos(datos_viejos,datos_nuevos)
    except:
      datos = datos_viejos
    
    modelos = crear_modelos(configuracion.tipo_modelo)
    pipeline = cargar_pipeline()

    columnas_a_eliminar = configuracion.columnas_diagnostico
    datos_procesados_filtrado = datos.drop(columns=columnas_a_eliminar)
    datos_pipeline_x = pipeline.transform(datos_procesados_filtrado)

    try:
      resultado, puntajes = reentrenar_modelos(modelos, datos_pipeline_x, datos)
    except:
      resultado = reentrenar_modelos(modelos, datos_pipeline_x, datos)

      return render(request,'error.html',{
        'error': resultado #ocurrio algun error asociado al entrenamiento de los modelos
      })
    
    if resultado == 1:
      try:
        guardar_datos = post_datos(datos_nuevos)
        if guardar_datos == False:
          return render(request,'error.html',{
            # no se guardan los datos pero el modelo se reentreno, significa que hay un posible error en el google sheets
            'error':'No se han podido guardar los datos correctamente, a pesar de que el modelo se reentrenó exitosamente'
          })
      except:
        pass

      try:
        auxiliar_subir_archivos()
      except:
        return render(request,'error.html',{
          # no se guardan los modelos aunque se reentrenaron, revisar el google drive
          'error':'No se han podido subir los modelos a Drive, a pesar de que los reentrenamientos se realizaron exitosamente'
        })
      
      return render(request,'acierto.html',{
        'informacion':"Los modelos se han reentrenado con éxito",
        'mialgia_puntaje': round(puntajes[0], 2),
        'dMiofacial_puntaje': round(puntajes[1], 2),
        'artralgiaI_puntaje': round(puntajes[2], 2),
        'artralgiaD_puntaje': round(puntajes[3], 2),
        'cReduccionI_puntaje': round(puntajes[4], 2),
        'cReduccionD_puntaje': round(puntajes[5], 2),
      })

    else:
      return render(request,'error.html',{
        'error':resultado
      })
    
"""

Funcion auxiliar para reconvertir los valores del excel que eran numericos anteriormente

"""
    
def convertir_numerico(cell):
  try:
    return pd.to_numeric(cell)
  except (ValueError, TypeError):
    return cell
  
"""

Get para traer los datos actuales almacenados en google sheets

"""
    
def get_datos():
  url = secretos["URL"]
  response = requests.get(url)
  datos_viejos = None
  columnas = configuracion.columnas + configuracion.columnas_diagnostico
  if response.status_code == 200:
    data = response.json()

    columnas = data[0]
    filas = data[1:]

    datos_viejos = pd.DataFrame(filas, columns=columnas)
    datos_viejos = datos_viejos.apply(lambda col: col.map(convertir_numerico))
  else:
    print(f'Error en la solicitud: {response.status_code}')

  return datos_viejos

"""

Post para enviar los nuevos datos a google sheets

"""

def post_datos(datos):
  try:
    #se manejan 2 casos, cuando se ingresa el excel y se maneja un dataframe, o cuando se quiere subir el diagnostico (una lista)
    try:
      data = datos.values.tolist()
    except:
      data = [datos]

    post_data = {
      "data": data
    }

    json_data = json.dumps(post_data)
    url = secretos["URL"]
    
    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
    
    if response.status_code != 200:
      print("Error:", response.text)
      return False
    else: 
      print("Éxito:", response.text)
      return True
  
  except requests.exceptions.RequestException as e:
    return(f"Error al realizar la solicitud: {e}")

"""

Funciones para manejar algunas vistas

"""

def index(request):
  return render(request,'index.html')

def reentrenar_modelo(request):
  return render(request,'reentrenar.html')

@login_required
def user_logout(request):
  logout(request)
  return HttpResponseRedirect(reverse('index'))

@login_required
def diagnosticar(request):
  form = DatosDiagnostico()
  return render(request,'diagnosticar.html',{'form':form})

"""

Apartado para cargar los archivos de los modelos de google drive

"""

def iniciar_sesion_drive():
  credenciales_json = {
    "type": secretos["GOOGLE_TYPE"],
    "project_id": secretos["GOOGLE_PROJECT_ID"],
    "private_key_id": secretos["GOOGLE_PRIVATE_KEY_ID"],
    "private_key": secretos["GOOGLE_PRIVATE_KEY"],
    "client_email": secretos["GOOGLE_CLIENT_EMAIL"],
    "client_id": secretos["GOOGLE_CLIENT_ID"],
    "auth_uri": secretos["GOOGLE_AUTH_URI"],
    "token_uri": secretos["GOOGLE_TOKEN_URI"],
    "auth_provider_x509_cert_url": secretos["GOOGLE_AUTH_PROVIDER_CERT_URL"],
    "client_x509_cert_url": secretos["GOOGLE_CLIENT_CERT_URL"],
    "universe_domain": secretos["GOOGLE_UNIVERSE_DOMAIN"]
  }
  
  SCOPES = ['https://www.googleapis.com/auth/drive']
  credenciales = service_account.Credentials.from_service_account_info(credenciales_json, scopes=SCOPES)
  servicio = build('drive', 'v3', credentials=credenciales)
  return servicio

def descargar_archivo(id_archivo, ruta, nombre_archivo):
  servicio = iniciar_sesion_drive()

  request = servicio.files().get_media(fileId=id_archivo)
  with open(ruta, 'wb') as archivo:
    downloader = googleapiclient.http.MediaIoBaseDownload(archivo, request)
    
    done = False
    while not done:
      status, done = downloader.next_chunk()
      print("Progreso descarga archivo "+ nombre_archivo +" "+ "%d%%." % int(status.progress() * 100))

def descargar_archivo_drive(nombre_archivo):
  ruta = 'modelos/{}'.format(nombre_archivo)
  id_carpeta = secretos["DRIVE_FOLDER_ID"]
  servicio = iniciar_sesion_drive()
  archivo = buscar_archivo_por_nombre(servicio, nombre_archivo, id_carpeta)
  id_archivo = archivo["id"]
  descargar_archivo(id_archivo, ruta, nombre_archivo)
  return True

"""

Apartado para subir los archivos de los modelos a google drive

"""

def buscar_archivo_por_nombre(servicio, nombre_archivo, carpeta_id):
  query = f"name='{nombre_archivo}' and '{carpeta_id}' in parents and trashed=false"
  resultados = servicio.files().list(q=query, fields="files(id, name)").execute()
  archivos = resultados.get('files', [])
  return archivos[0] if archivos else None

def subir_archivo(nombre_archivo, ruta, carpeta_id, mime_type='application/octet-stream'):
  servicio = iniciar_sesion_drive()
  
  archivo_existente = buscar_archivo_por_nombre(servicio, nombre_archivo, carpeta_id)

  if archivo_existente:
    media = MediaFileUpload(ruta, mimetype=mime_type)
    archivo_actualizado = servicio.files().update(
        fileId=archivo_existente['id'],
        media_body=media
    ).execute()
    return archivo_actualizado.get('id')

def subir_archivo_drive(nombre, ruta):
  nombre_archivo = nombre
  ruta_archivo = ruta
  id_carpeta = secretos["DRIVE_FOLDER_ID"]
  mime_type = 'application/octet-stream'
  id_archivo = subir_archivo(nombre_archivo, ruta_archivo, id_carpeta, mime_type)

def auxiliar_subir_archivos():
  subir_modelos = configuracion.nombres_modelos
  for modelo in subir_modelos:
    subir_archivo_drive(modelo, "modelos/" + modelo)

"""

Cargar archivos del modelo cuando empieza la aplicacion

"""

descargar_modelos = configuracion.nombres_modelos

for modelo in descargar_modelos:
  descargar_archivo_drive(modelo)
