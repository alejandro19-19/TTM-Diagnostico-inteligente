from .primera_parte import *
from .segunda_parte import *

def convertir_datos(datos):  
  datos_procesados = []
  #primera parte
  uno_a_derecho = convertir_primera_parte_a(datos.cleaned_data['localizacion_dolor_derecho'])
  uno_a_izquierdo = convertir_primera_parte_a(datos.cleaned_data['localizacion_dolor_izquierdo'])
  uno_b_derecho = convertir_primera_parte_b(datos.cleaned_data['localizacion_cefalea_derecho'])
  uno_b_izquierdo = convertir_primera_parte_b(datos.cleaned_data['localizacion_cefalea_izquierdo'])
  
  #segunda parte
  diente_referencia = [datos.cleaned_data['diente_referencia']]
  sobre_mordida_horizontal = [datos.cleaned_data['sobre_mordida_horizontal']]
  sobre_mordida_vertical = [datos.cleaned_data['sobre_mordida_vertical']]
  desviacion_linea_media_lado = convertir_segunda_parte(datos.cleaned_data['desviacion_linea_media'],datos.cleaned_data['desviacion_linea_lado'])
  
  #tercera parte
  patron_apertura = [datos.cleaned_data['patron_apertura']]
  lado_apertura = [datos.cleaned_data['lado_apertura']]

  #cuarta parte
  apertura_sin_dolor = [int(datos.cleaned_data['apertura_sin_dolor'])]
  apertura_maxima_no_asistida = [int(datos.cleaned_data['apertura_maxima_no_asistida'])]
  apertura_Maxima_Asistida = [int(datos.cleaned_data['apertura_Maxima_Asistida'])]
  terminada = [datos.cleaned_data['terminada']]
  temporal_dolor_derecho_1_4 = [datos.cleaned_data['temporal_dolor_derecho_1_4']]
  temporal_dolor_familiar_derecho_1_4 = [datos.cleaned_data['temporal_dolor_familiar_derecho_1_4']]
  temporal_cefalea_familiar_derecho_1_4 = [datos.cleaned_data['temporal_cefalea_familiar_derecho_1_4']]
  masetero_dolor_derecho_1_4 = [datos.cleaned_data['masetero_dolor_derecho_1_4']]
  masetero_dolor_familiar_derecho_1_4 = [datos.cleaned_data['masetero_dolor_familiar_derecho_1_4']]
  ATM_dolor_derecho_1_4 = [datos.cleaned_data['ATM_dolor_derecho_1_4']]
  ATM_dolor_familiar_derecho_1_4 = [datos.cleaned_data['ATM_dolor_familiar_derecho_1_4']]
  otros_Musc_M_dolor_derecho_1_4 = [datos.cleaned_data['otros_Musc_M_dolor_derecho_1_4']]
  otros_Musc_M_dolor_familiar_derecho_1_4 = [datos.cleaned_data['otros_Musc_M_dolor_familiar_derecho_1_4']]
  no_Masticat_dolor_derecho_1_4 = [datos.cleaned_data['no_Masticat_dolor_derecho_1_4']]
  no_Masticat_dolor_familiar_derecho_1_4 = [datos.cleaned_data['no_Masticat_dolor_familiar_derecho_1_4']]
  temporal_dolor_derecho_2_4 = [datos.cleaned_data['temporal_dolor_derecho_2_4']]
  temporal_dolor_familiar_derecho_2_4 = [datos.cleaned_data['temporal_dolor_familiar_derecho_2_4']]
  temporal_cefalea_familiar_derecho_2_4 = [datos.cleaned_data['temporal_cefalea_familiar_derecho_2_4']]
  masetero_dolor_derecho_2_4 = [datos.cleaned_data['masetero_dolor_derecho_2_4']]
  masetero_dolor_familiar_derecho_2_4 = [datos.cleaned_data['masetero_dolor_familiar_derecho_2_4']]
  ATM_dolor_derecho_2_4 = [datos.cleaned_data['ATM_dolor_derecho_2_4']]
  ATM_dolor_familiar_derecho_2_4 = [datos.cleaned_data['ATM_dolor_familiar_derecho_2_4']]
  otros_Musc_M_dolor_derecho_2_4 = [datos.cleaned_data['otros_Musc_M_dolor_derecho_2_4']]
  otros_Musc_M_dolor_familiar_derecho_2_4 = [datos.cleaned_data['otros_Musc_M_dolor_familiar_derecho_2_4']]
  no_Masticat_dolor_derecho_2_4 = [datos.cleaned_data['no_Masticat_dolor_derecho_2_4']]
  no_Masticat_dolor_familiar_derecho_2_4 = [datos.cleaned_data['no_Masticat_dolor_familiar_derecho_2_4']]
  temporal_dolor_izquierdo_1_4 = [datos.cleaned_data['temporal_dolor_izquierdo_1_4']]
  temporal_dolor_familiar_izquierdo_1_4 = [datos.cleaned_data['temporal_dolor_familiar_izquierdo_1_4']]
  temporal_cefalea_familiar_izquierdo_1_4 = [datos.cleaned_data['temporal_cefalea_familiar_izquierdo_1_4']]
  masetero_dolor_izquierdo_1_4 = [datos.cleaned_data['masetero_dolor_izquierdo_1_4']]
  masetero_dolor_familiar_izquierdo_1_4 = [datos.cleaned_data['masetero_dolor_familiar_izquierdo_1_4']]
  ATM_dolor_izquierdo_1_4 = [datos.cleaned_data['ATM_dolor_izquierdo_1_4']]
  ATM_dolor_familiar_izquierdo_1_4 = [datos.cleaned_data['ATM_dolor_familiar_izquierdo_1_4']]
  otros_Musc_M_dolor_izquierdo_1_4 = [datos.cleaned_data['otros_Musc_M_dolor_izquierdo_1_4']]
  otros_Musc_M_dolor_familiar_izquierdo_1_4 = [datos.cleaned_data['otros_Musc_M_dolor_familiar_izquierdo_1_4']]
  no_Masticat_dolor_izquierdo_1_4 = [datos.cleaned_data['no_Masticat_dolor_izquierdo_1_4']]
  no_Masticat_dolor_familiar_izquierdo_1_4 = [datos.cleaned_data['no_Masticat_dolor_familiar_izquierdo_1_4']]
  temporal_dolor_izquierdo_2_4 = [datos.cleaned_data['temporal_dolor_izquierdo_2_4']]
  temporal_dolor_familiar_izquierdo_2_4 = [datos.cleaned_data['temporal_dolor_familiar_izquierdo_2_4']]
  temporal_cefalea_familiar_izquierdo_2_4 = [datos.cleaned_data['temporal_cefalea_familiar_izquierdo_2_4']]
  masetero_dolor_izquierdo_2_4 = [datos.cleaned_data['masetero_dolor_izquierdo_2_4']]
  masetero_dolor_familiar_izquierdo_2_4 = [datos.cleaned_data['masetero_dolor_familiar_izquierdo_2_4']]
  ATM_dolor_izquierdo_2_4 = [datos.cleaned_data['ATM_dolor_izquierdo_2_4']]
  ATM_dolor_familiar_izquierdo_2_4 = [datos.cleaned_data['ATM_dolor_familiar_izquierdo_2_4']]
  otros_Musc_M_dolor_izquierdo_2_4 = [datos.cleaned_data['otros_Musc_M_dolor_izquierdo_2_4']]
  otros_Musc_M_dolor_familiar_izquierdo_2_4 = [datos.cleaned_data['otros_Musc_M_dolor_familiar_izquierdo_2_4']]
  no_Masticat_dolor_izquierdo_2_4 = [datos.cleaned_data['no_Masticat_dolor_izquierdo_2_4']]
  no_Masticat_dolor_familiar_izquierdo_2_4 = [datos.cleaned_data['no_Masticat_dolor_familiar_izquierdo_2_4']]

  #quinta parte
  lateralidad_derecha = [int(datos.cleaned_data['lateralidad_derecha'])]
  lateralidad_izquierda = [int(datos.cleaned_data['lateralidad_izquierda'])]
  protusion = [int(datos.cleaned_data['protusion'])]
  temporal_dolor_derecho_1_5 = [datos.cleaned_data['temporal_dolor_derecho_1_5']]
  temporal_dolor_familiar_derecho_1_5 = [datos.cleaned_data['temporal_dolor_familiar_derecho_1_5']]
  temporal_cefalea_familiar_derecho_1_5 = [datos.cleaned_data['temporal_cefalea_familiar_derecho_1_5']]
  masetero_dolor_derecho_1_5 = [datos.cleaned_data['masetero_dolor_derecho_1_5']]
  masetero_dolor_familiar_derecho_1_5 = [datos.cleaned_data['masetero_dolor_familiar_derecho_1_5']]
  ATM_dolor_derecho_1_5 = [datos.cleaned_data['ATM_dolor_derecho_1_5']]
  ATM_dolor_familiar_derecho_1_5 = [datos.cleaned_data['ATM_dolor_familiar_derecho_1_5']]
  otros_Musc_M_dolor_derecho_1_5 = [datos.cleaned_data['otros_Musc_M_dolor_derecho_1_5']]
  otros_Musc_M_dolor_familiar_derecho_1_5 = [datos.cleaned_data['otros_Musc_M_dolor_familiar_derecho_1_5']]
  no_Masticat_dolor_derecho_1_5 = [datos.cleaned_data['no_Masticat_dolor_derecho_1_5']]
  no_Masticat_dolor_familiar_derecho_1_5 = [datos.cleaned_data['no_Masticat_dolor_familiar_derecho_1_5']]
  temporal_dolor_derecho_2_5 = [datos.cleaned_data['temporal_dolor_derecho_2_5']]
  temporal_dolor_familiar_derecho_2_5 = [datos.cleaned_data['temporal_dolor_familiar_derecho_2_5']]
  temporal_cefalea_familiar_derecho_2_5 = [datos.cleaned_data['temporal_cefalea_familiar_derecho_2_5']]
  masetero_dolor_derecho_2_5 = [datos.cleaned_data['masetero_dolor_derecho_2_5']]
  masetero_dolor_familiar_derecho_2_5 = [datos.cleaned_data['masetero_dolor_familiar_derecho_2_5']]
  ATM_dolor_derecho_2_5 = [datos.cleaned_data['ATM_dolor_derecho_2_5']]
  ATM_dolor_familiar_derecho_2_5 = [datos.cleaned_data['ATM_dolor_familiar_derecho_2_5']]
  otros_Musc_M_dolor_derecho_2_5 = [datos.cleaned_data['otros_Musc_M_dolor_derecho_2_5']]
  otros_Musc_M_dolor_familiar_derecho_2_5 = [datos.cleaned_data['otros_Musc_M_dolor_familiar_derecho_2_5']]
  no_Masticat_dolor_derecho_2_5 = [datos.cleaned_data['no_Masticat_dolor_derecho_2_5']]
  no_Masticat_dolor_familiar_derecho_2_5 = [datos.cleaned_data['no_Masticat_dolor_familiar_derecho_2_5']]
  temporal_dolor_derecho_3_5 = [datos.cleaned_data['temporal_dolor_derecho_3_5']]
  temporal_dolor_familiar_derecho_3_5 = [datos.cleaned_data['temporal_dolor_familiar_derecho_3_5']]
  temporal_cefalea_familiar_derecho_3_5 = [datos.cleaned_data['temporal_cefalea_familiar_derecho_3_5']]
  masetero_dolor_derecho_3_5 = [datos.cleaned_data['masetero_dolor_derecho_3_5']]
  masetero_dolor_familiar_derecho_3_5 = [datos.cleaned_data['masetero_dolor_familiar_derecho_3_5']]
  ATM_dolor_derecho_3_5 = [datos.cleaned_data['ATM_dolor_derecho_3_5']]
  ATM_dolor_familiar_derecho_3_5 = [datos.cleaned_data['ATM_dolor_familiar_derecho_3_5']]
  otros_Musc_M_dolor_derecho_3_5 = [datos.cleaned_data['otros_Musc_M_dolor_derecho_3_5']]
  otros_Musc_M_dolor_familiar_derecho_3_5 = [datos.cleaned_data['otros_Musc_M_dolor_familiar_derecho_3_5']]
  no_Masticat_dolor_derecho_3_5 = [datos.cleaned_data['no_Masticat_dolor_derecho_3_5']]
  no_Masticat_dolor_familiar_derecho_3_5 = [datos.cleaned_data['no_Masticat_dolor_familiar_derecho_3_5']]
  temporal_dolor_izquierdo_1_5 = [datos.cleaned_data['temporal_dolor_izquierdo_1_5']]
  temporal_dolor_familiar_izquierdo_1_5 = [datos.cleaned_data['temporal_dolor_familiar_izquierdo_1_5']]
  temporal_cefalea_familiar_izquierdo_1_5 = [datos.cleaned_data['temporal_cefalea_familiar_izquierdo_1_5']]
  masetero_dolor_izquierdo_1_5 = [datos.cleaned_data['masetero_dolor_izquierdo_1_5']]
  masetero_dolor_familiar_izquierdo_1_5 = [datos.cleaned_data['masetero_dolor_familiar_izquierdo_1_5']]
  ATM_dolor_izquierdo_1_5 = [datos.cleaned_data['ATM_dolor_izquierdo_1_5']]
  ATM_dolor_familiar_izquierdo_1_5 = [datos.cleaned_data['ATM_dolor_familiar_izquierdo_1_5']]
  otros_Musc_M_dolor_izquierdo_1_5 = [datos.cleaned_data['otros_Musc_M_dolor_izquierdo_1_5']]
  otros_Musc_M_dolor_familiar_izquierdo_1_5 = [datos.cleaned_data['otros_Musc_M_dolor_familiar_izquierdo_1_5']]
  no_Masticat_dolor_izquierdo_1_5 = [datos.cleaned_data['no_Masticat_dolor_izquierdo_1_5']]
  no_Masticat_dolor_familiar_izquierdo_1_5 = [datos.cleaned_data['no_Masticat_dolor_familiar_izquierdo_1_5']]
  temporal_dolor_izquierdo_2_5 = [datos.cleaned_data['temporal_dolor_izquierdo_2_5']]
  temporal_dolor_familiar_izquierdo_2_5 = [datos.cleaned_data['temporal_dolor_familiar_izquierdo_2_5']]
  temporal_cefalea_familiar_izquierdo_2_5 = [datos.cleaned_data['temporal_cefalea_familiar_izquierdo_2_5']]
  masetero_dolor_izquierdo_2_5 = [datos.cleaned_data['masetero_dolor_izquierdo_2_5']]
  masetero_dolor_familiar_izquierdo_2_5 = [datos.cleaned_data['masetero_dolor_familiar_izquierdo_2_5']]
  ATM_dolor_izquierdo_2_5 = [datos.cleaned_data['ATM_dolor_izquierdo_2_5']]
  ATM_dolor_familiar_izquierdo_2_5 = [datos.cleaned_data['ATM_dolor_familiar_izquierdo_2_5']]
  otros_Musc_M_dolor_izquierdo_2_5 = [datos.cleaned_data['otros_Musc_M_dolor_izquierdo_2_5']]
  otros_Musc_M_dolor_familiar_izquierdo_2_5 = [datos.cleaned_data['otros_Musc_M_dolor_familiar_izquierdo_2_5']]
  no_Masticat_dolor_izquierdo_2_5 = [datos.cleaned_data['no_Masticat_dolor_izquierdo_2_5']]
  no_Masticat_dolor_familiar_izquierdo_2_5 = [datos.cleaned_data['no_Masticat_dolor_familiar_izquierdo_2_5']]
  temporal_dolor_izquierdo_3_5 = [datos.cleaned_data['temporal_dolor_izquierdo_3_5']]
  temporal_dolor_familiar_izquierdo_3_5 = [datos.cleaned_data['temporal_dolor_familiar_izquierdo_3_5']]
  temporal_cefalea_familiar_izquierdo_3_5 = [datos.cleaned_data['temporal_cefalea_familiar_izquierdo_3_5']]
  masetero_dolor_izquierdo_3_5 = [datos.cleaned_data['masetero_dolor_izquierdo_3_5']]
  masetero_dolor_familiar_izquierdo_3_5 = [datos.cleaned_data['masetero_dolor_familiar_izquierdo_3_5']]
  ATM_dolor_izquierdo_3_5 = [datos.cleaned_data['ATM_dolor_izquierdo_3_5']]
  ATM_dolor_familiar_izquierdo_3_5 = [datos.cleaned_data['ATM_dolor_familiar_izquierdo_3_5']]
  otros_Musc_M_dolor_izquierdo_3_5 = [datos.cleaned_data['otros_Musc_M_dolor_izquierdo_3_5']]
  otros_Musc_M_dolor_familiar_izquierdo_3_5 = [datos.cleaned_data['otros_Musc_M_dolor_familiar_izquierdo_3_5']]
  no_Masticat_dolor_izquierdo_3_5 = [datos.cleaned_data['no_Masticat_dolor_izquierdo_3_5']]
  no_Masticat_dolor_familiar_izquierdo_3_5 = [datos.cleaned_data['no_Masticat_dolor_familiar_izquierdo_3_5']]

  #sexta parte
  click_apertura_derecho_6 = [datos.cleaned_data['click_apertura_derecho_6']]
  click_cierre_derecho_6 = [datos.cleaned_data['click_cierre_derecho_6']]
  click_paciente_derecho_6 = [datos.cleaned_data['click_paciente_derecho_6']]
  click_dolor_derecho_6 = [datos.cleaned_data['click_dolor_derecho_6']]
  click_dolor_familiar_derecho_6 = [datos.cleaned_data['click_dolor_familiar_derecho_6']]
  crepitacion_apertura_derecho_6 = [datos.cleaned_data['crepitacion_apertura_derecho_6']]
  crepitacion_cierre_derecho_6 = [datos.cleaned_data['crepitacion_cierre_derecho_6']]
  crepitacion_paciente_derecho_6 = [datos.cleaned_data['crepitacion_paciente_derecho_6']]
  click_apertura_izquierdo_6 = [datos.cleaned_data['click_apertura_izquierdo_6']]
  click_cierre_izquierdo_6 = [datos.cleaned_data['click_cierre_izquierdo_6']]
  click_paciente_izquierdo_6 = [datos.cleaned_data['click_paciente_izquierdo_6']]
  click_dolor_izquierdo_6 = [datos.cleaned_data['click_dolor_izquierdo_6']]
  click_dolor_familiar_izquierdo_6 = [datos.cleaned_data['click_dolor_familiar_izquierdo_6']]
  crepitacion_apertura_izquierdo_6 = [datos.cleaned_data['crepitacion_apertura_izquierdo_6']]
  crepitacion_cierre_izquierdo_6 = [datos.cleaned_data['crepitacion_cierre_izquierdo_6']]
  crepitacion_paciente_izquierdo_6 = [datos.cleaned_data['crepitacion_paciente_izquierdo_6']]
  
  
  #septima parte

  click_examinador_derecho_7 = [datos.cleaned_data['click_examinador_derecho_7']]
  click_paciente_derecho_7 = [datos.cleaned_data['click_paciente_derecho_7']]
  click_dolor_derecho_7 = [datos.cleaned_data['click_dolor_derecho_7']]
  click_dolor_familiar_derecho_7 = [datos.cleaned_data['click_dolor_familiar_derecho_7']]
  crepitacion_examinador_derecho_7 = [datos.cleaned_data['crepitacion_examinador_derecho_7']]
  crepitacion_paciente_derecho_7 = [datos.cleaned_data['crepitacion_paciente_derecho_7']]
  click_examinador_izquierdo_7 = [datos.cleaned_data['click_examinador_izquierdo_7']]
  click_paciente_izquierdo_7 = [datos.cleaned_data['click_paciente_izquierdo_7']]
  click_dolor_izquierdo_7 = [datos.cleaned_data['click_dolor_izquierdo_7']]
  click_dolor_familiar_izquierdo_7 = [datos.cleaned_data['click_dolor_familiar_izquierdo_7']]
  crepitacion_examinador_izquierdo_7 = [datos.cleaned_data['crepitacion_examinador_izquierdo_7']]
  crepitacion_paciente_izquierdo_7 = [datos.cleaned_data['crepitacion_paciente_izquierdo_7']]

  #octava parte
  mientras_abre_bloqueo_derecho_8 = [datos.cleaned_data['mientras_abre_bloqueo_derecho_8']]
  mientras_abre_paciente_derecho_8 = [datos.cleaned_data['mientras_abre_paciente_derecho_8']]
  mientras_abre_evaluador_derecho_8 = [datos.cleaned_data['mientras_abre_evaluador_derecho_8']]
  posicion_max_apertura_bloqueo_derecho_8 = [datos.cleaned_data['posicion_max_apertura_bloqueo_derecho_8']]
  posicion_max_apertura_paciente_derecho_8 = [datos.cleaned_data['posicion_max_apertura_paciente_derecho_8']]
  posicion_max_apertura_evaluador_derecho_8 = [datos.cleaned_data['posicion_max_apertura_evaluador_derecho_8']]
  mientras_abre_bloqueo_izquierdo_8 = [datos.cleaned_data['mientras_abre_bloqueo_izquierdo_8']]
  mientras_abre_paciente_izquierdo_8 = [datos.cleaned_data['mientras_abre_paciente_izquierdo_8']]
  mientras_abre_evaluador_izquierdo_8 = [datos.cleaned_data['mientras_abre_evaluador_izquierdo_8']]
  posicion_max_apertura_bloqueo_izquierdo_8 = [datos.cleaned_data['posicion_max_apertura_bloqueo_izquierdo_8']]
  posicion_max_apertura_paciente_izquierdo_8 = [datos.cleaned_data['posicion_max_apertura_paciente_izquierdo_8']]
  posicion_max_apertura_evaluador_izquierdo_8 = [datos.cleaned_data['posicion_max_apertura_evaluador_izquierdo_8']]

  #novena parte
  posterior_dolor_derecho_9 = [datos.cleaned_data['posterior_dolor_derecho_9']]
  posterior_dolor_familiar_derecho_9 = [datos.cleaned_data['posterior_dolor_familiar_derecho_9']]
  posterior_cefalea_familiar_derecho_9 = [datos.cleaned_data['posterior_cefalea_familiar_derecho_9']]
  posterior_dolor_referido_derecho_9 = [datos.cleaned_data['posterior_dolor_referido_derecho_9']]
  medio_dolor_derecho_9 = [datos.cleaned_data['medio_dolor_derecho_9']]
  medio_dolor_familiar_derecho_9 = [datos.cleaned_data['medio_dolor_familiar_derecho_9']]
  medio_cefalea_familiar_derecho_9 = [datos.cleaned_data['medio_cefalea_familiar_derecho_9']]
  medio_dolor_referido_derecho_9 = [datos.cleaned_data['medio_dolor_referido_derecho_9']]
  anterior_dolor_derecho_9 = [datos.cleaned_data['anterior_dolor_derecho_9']]
  anterior_dolor_familiar_derecho_9 = [datos.cleaned_data['anterior_dolor_familiar_derecho_9']]
  anterior_cefalea_familiar_derecho_9 = [datos.cleaned_data['anterior_cefalea_familiar_derecho_9']]
  anterior_dolor_referido_derecho_9 = [datos.cleaned_data['anterior_dolor_referido_derecho_9']]
  origen_dolor_derecho_9 = [datos.cleaned_data['origen_dolor_derecho_9']]
  origen_dolor_familiar_derecho_9 = [datos.cleaned_data['origen_dolor_familiar_derecho_9']]
  origen_dolor_referido_derecho_9 = [datos.cleaned_data['origen_dolor_referido_derecho_9']]
  cuerpo_dolor_derecho_9 = [datos.cleaned_data['cuerpo_dolor_derecho_9']]
  cuerpo_dolor_familiar_derecho_9 = [datos.cleaned_data['cuerpo_dolor_familiar_derecho_9']]
  cuerpo_dolor_referido_derecho_9 = [datos.cleaned_data['cuerpo_dolor_referido_derecho_9']]
  insercion_dolor_derecho_9 = [datos.cleaned_data['insercion_dolor_derecho_9']]
  insercion_dolor_familiar_derecho_9 = [datos.cleaned_data['insercion_dolor_familiar_derecho_9']]
  insercion_dolor_referido_derecho_9 = [datos.cleaned_data['insercion_dolor_referido_derecho_9']]
  lateral_dolor_derecho_9 = [datos.cleaned_data['lateral_dolor_derecho_9']]
  lateral_dolor_familiar_derecho_9 = [datos.cleaned_data['lateral_dolor_familiar_derecho_9']]
  lateral_dolor_referido_derecho_9 = [datos.cleaned_data['lateral_dolor_referido_derecho_9']]
  alrededor_dolor_derecho_9 = [datos.cleaned_data['alrededor_dolor_derecho_9']]
  alrededor_dolor_familiar_derecho_9 = [datos.cleaned_data['alrededor_dolor_familiar_derecho_9']]
  alrededor_dolor_referido_derecho_9 = [datos.cleaned_data['alrededor_dolor_referido_derecho_9']]
  posterior_dolor_izquierdo_9 = [datos.cleaned_data['posterior_dolor_izquierdo_9']]
  posterior_dolor_familiar_izquierdo_9 = [datos.cleaned_data['posterior_dolor_familiar_izquierdo_9']]
  posterior_cefalea_familiar_izquierdo_9 = [datos.cleaned_data['posterior_cefalea_familiar_izquierdo_9']]
  posterior_dolor_referido_izquierdo_9 = [datos.cleaned_data['posterior_dolor_referido_izquierdo_9']]
  medio_dolor_izquierdo_9 = [datos.cleaned_data['medio_dolor_izquierdo_9']]
  medio_dolor_familiar_izquierdo_9 = [datos.cleaned_data['medio_dolor_familiar_izquierdo_9']]
  medio_cefalea_familiar_izquierdo_9 = [datos.cleaned_data['medio_cefalea_familiar_izquierdo_9']]
  medio_dolor_referido_izquierdo_9 = [datos.cleaned_data['medio_dolor_referido_izquierdo_9']]
  anterior_dolor_izquierdo_9 = [datos.cleaned_data['anterior_dolor_izquierdo_9']]
  anterior_dolor_familiar_izquierdo_9 = [datos.cleaned_data['anterior_dolor_familiar_izquierdo_9']]
  anterior_cefalea_familiar_izquierdo_9 = [datos.cleaned_data['anterior_cefalea_familiar_izquierdo_9']]
  anterior_dolor_referido_izquierdo_9 = [datos.cleaned_data['anterior_dolor_referido_izquierdo_9']]
  origen_dolor_izquierdo_9 = [datos.cleaned_data['origen_dolor_izquierdo_9']]
  origen_dolor_familiar_izquierdo_9 = [datos.cleaned_data['origen_dolor_familiar_izquierdo_9']]
  origen_dolor_referido_izquierdo_9 = [datos.cleaned_data['origen_dolor_referido_izquierdo_9']]
  cuerpo_dolor_izquierdo_9 = [datos.cleaned_data['cuerpo_dolor_izquierdo_9']]
  cuerpo_dolor_familiar_izquierdo_9 = [datos.cleaned_data['cuerpo_dolor_familiar_izquierdo_9']]
  cuerpo_dolor_referido_izquierdo_9 = [datos.cleaned_data['cuerpo_dolor_referido_izquierdo_9']]
  insercion_dolor_izquierdo_9 = [datos.cleaned_data['insercion_dolor_izquierdo_9']]
  insercion_dolor_familiar_izquierdo_9 = [datos.cleaned_data['insercion_dolor_familiar_izquierdo_9']]
  insercion_dolor_referido_izquierdo_9 = [datos.cleaned_data['insercion_dolor_referido_izquierdo_9']]
  lateral_dolor_izquierdo_9 = [datos.cleaned_data['lateral_dolor_izquierdo_9']]
  lateral_dolor_familiar_izquierdo_9 = [datos.cleaned_data['lateral_dolor_familiar_izquierdo_9']]
  lateral_dolor_referido_izquierdo_9 = [datos.cleaned_data['lateral_dolor_referido_izquierdo_9']]
  alrededor_dolor_izquierdo_9 = [datos.cleaned_data['alrededor_dolor_izquierdo_9']]
  alrededor_dolor_familiar_izquierdo_9 = [datos.cleaned_data['alrededor_dolor_familiar_izquierdo_9']]
  alrededor_dolor_referido_izquierdo_9 = [datos.cleaned_data['alrededor_dolor_referido_izquierdo_9']]

  #decima parte
  mandibular_dolor_derecho_10 = [datos.cleaned_data['mandibular_dolor_derecho_10']]
  mandibular_dolor_familiar_derecho_10 = [datos.cleaned_data['mandibular_dolor_familiar_derecho_10']]
  mandibular_dolor_referido_derecho_10 = [datos.cleaned_data['mandibular_dolor_referido_derecho_10']]
  submandibular_dolor_derecho_10 = [datos.cleaned_data['submandibular_dolor_derecho_10']]
  submandibular_dolor_familiar_derecho_10 = [datos.cleaned_data['submandibular_dolor_familiar_derecho_10']]
  submandibular_dolor_referido_derecho_10 = [datos.cleaned_data['submandibular_dolor_referido_derecho_10']]
  lateral_dolor_derecho_10 = [datos.cleaned_data['lateral_dolor_derecho_10']]
  lateral_dolor_familiar_derecho_10 = [datos.cleaned_data['lateral_dolor_familiar_derecho_10']]
  lateral_dolor_referido_derecho_10 = [datos.cleaned_data['lateral_dolor_referido_derecho_10']]
  temporal_dolor_derecho_10 = [datos.cleaned_data['temporal_dolor_derecho_10']]
  temporal_dolor_familiar_derecho_10 = [datos.cleaned_data['temporal_dolor_familiar_derecho_10']]
  temporal_dolor_referido_derecho_10 = [datos.cleaned_data['temporal_dolor_referido_derecho_10']]
  mandibular_dolor_izquierdo_10 = [datos.cleaned_data['mandibular_dolor_izquierdo_10']]
  mandibular_dolor_familiar_izquierdo_10 = [datos.cleaned_data['mandibular_dolor_familiar_izquierdo_10']]
  mandibular_dolor_referido_izquierdo_10 = [datos.cleaned_data['mandibular_dolor_referido_izquierdo_10']]
  submandibular_dolor_izquierdo_10 = [datos.cleaned_data['submandibular_dolor_izquierdo_10']]
  submandibular_dolor_familiar_izquierdo_10 = [datos.cleaned_data['submandibular_dolor_familiar_izquierdo_10']]
  submandibular_dolor_referido_izquierdo_10 = [datos.cleaned_data['submandibular_dolor_referido_izquierdo_10']]
  lateral_dolor_izquierdo_10 = [datos.cleaned_data['lateral_dolor_izquierdo_10']]
  lateral_dolor_familiar_izquierdo_10 = [datos.cleaned_data['lateral_dolor_familiar_izquierdo_10']]
  lateral_dolor_referido_izquierdo_10 = [datos.cleaned_data['lateral_dolor_referido_izquierdo_10']]
  temporal_dolor_izquierdo_10 = [datos.cleaned_data['temporal_dolor_izquierdo_10']]
  temporal_dolor_familiar_izquierdo_10 = [datos.cleaned_data['temporal_dolor_familiar_izquierdo_10']]
  temporal_dolor_referido_izquierdo_10 = [datos.cleaned_data['temporal_dolor_referido_izquierdo_10']]


  datos_procesados = uno_a_derecho + uno_a_izquierdo + uno_b_derecho + uno_b_izquierdo
  

  datos_procesados = datos_procesados + diente_referencia + sobre_mordida_horizontal + sobre_mordida_vertical + desviacion_linea_media_lado


  datos_procesados = datos_procesados + patron_apertura + lado_apertura


  datos_procesados = datos_procesados + apertura_sin_dolor + apertura_maxima_no_asistida + apertura_Maxima_Asistida + terminada
  datos_procesados = datos_procesados + temporal_dolor_derecho_1_4 + temporal_dolor_familiar_derecho_1_4 + temporal_cefalea_familiar_derecho_1_4
  datos_procesados = datos_procesados + masetero_dolor_derecho_1_4 + masetero_dolor_familiar_derecho_1_4 + ATM_dolor_derecho_1_4
  datos_procesados = datos_procesados + ATM_dolor_familiar_derecho_1_4 + otros_Musc_M_dolor_derecho_1_4 + otros_Musc_M_dolor_familiar_derecho_1_4 
  datos_procesados = datos_procesados + no_Masticat_dolor_derecho_1_4 + no_Masticat_dolor_familiar_derecho_1_4 + temporal_dolor_derecho_2_4 
  datos_procesados = datos_procesados + temporal_dolor_familiar_derecho_2_4 + temporal_cefalea_familiar_derecho_2_4 + masetero_dolor_derecho_2_4
  datos_procesados = datos_procesados + masetero_dolor_familiar_derecho_2_4 + ATM_dolor_derecho_2_4 + ATM_dolor_familiar_derecho_2_4
  datos_procesados = datos_procesados + otros_Musc_M_dolor_derecho_2_4 + otros_Musc_M_dolor_familiar_derecho_2_4 + no_Masticat_dolor_derecho_2_4
  datos_procesados = datos_procesados + no_Masticat_dolor_familiar_derecho_2_4 + temporal_dolor_izquierdo_1_4 + temporal_dolor_familiar_izquierdo_1_4
  datos_procesados = datos_procesados + temporal_cefalea_familiar_izquierdo_1_4 + masetero_dolor_izquierdo_1_4 + masetero_dolor_familiar_izquierdo_1_4
  datos_procesados = datos_procesados + ATM_dolor_izquierdo_1_4 + ATM_dolor_familiar_izquierdo_1_4 + otros_Musc_M_dolor_izquierdo_1_4
  datos_procesados = datos_procesados + otros_Musc_M_dolor_familiar_izquierdo_1_4 + no_Masticat_dolor_izquierdo_1_4 + no_Masticat_dolor_familiar_izquierdo_1_4
  datos_procesados = datos_procesados + temporal_dolor_izquierdo_2_4 + temporal_dolor_familiar_izquierdo_2_4 + temporal_cefalea_familiar_izquierdo_2_4
  datos_procesados = datos_procesados + masetero_dolor_izquierdo_2_4 + masetero_dolor_familiar_izquierdo_2_4 + ATM_dolor_izquierdo_2_4
  datos_procesados = datos_procesados + ATM_dolor_familiar_izquierdo_2_4 + otros_Musc_M_dolor_izquierdo_2_4 + otros_Musc_M_dolor_familiar_izquierdo_2_4
  datos_procesados = datos_procesados + no_Masticat_dolor_izquierdo_2_4 + no_Masticat_dolor_familiar_izquierdo_2_4

  datos_procesados = datos_procesados + lateralidad_derecha + lateralidad_izquierda + protusion + temporal_dolor_derecho_1_5 + temporal_dolor_familiar_derecho_1_5
  datos_procesados = datos_procesados + temporal_cefalea_familiar_derecho_1_5 + masetero_dolor_derecho_1_5 + masetero_dolor_familiar_derecho_1_5
  datos_procesados = datos_procesados + ATM_dolor_derecho_1_5 + ATM_dolor_familiar_derecho_1_5 + otros_Musc_M_dolor_derecho_1_5 + otros_Musc_M_dolor_familiar_derecho_1_5
  datos_procesados = datos_procesados + no_Masticat_dolor_derecho_1_5 + no_Masticat_dolor_familiar_derecho_1_5 + temporal_dolor_derecho_2_5
  datos_procesados = datos_procesados + temporal_dolor_familiar_derecho_2_5 + temporal_cefalea_familiar_derecho_2_5 + masetero_dolor_derecho_2_5
  datos_procesados = datos_procesados + masetero_dolor_familiar_derecho_2_5 + ATM_dolor_derecho_2_5 + ATM_dolor_familiar_derecho_2_5
  datos_procesados = datos_procesados + otros_Musc_M_dolor_derecho_2_5 + otros_Musc_M_dolor_familiar_derecho_2_5 + no_Masticat_dolor_derecho_2_5
  datos_procesados = datos_procesados + no_Masticat_dolor_familiar_derecho_2_5 + temporal_dolor_derecho_3_5 + temporal_dolor_familiar_derecho_3_5
  datos_procesados = datos_procesados + temporal_cefalea_familiar_derecho_3_5 + masetero_dolor_derecho_3_5 + masetero_dolor_familiar_derecho_3_5
  datos_procesados = datos_procesados + ATM_dolor_derecho_3_5 + ATM_dolor_familiar_derecho_3_5 + otros_Musc_M_dolor_derecho_3_5 + otros_Musc_M_dolor_familiar_derecho_3_5
  datos_procesados = datos_procesados + no_Masticat_dolor_derecho_3_5 + no_Masticat_dolor_familiar_derecho_3_5 + temporal_dolor_izquierdo_1_5
  datos_procesados = datos_procesados + temporal_dolor_familiar_izquierdo_1_5 + temporal_cefalea_familiar_izquierdo_1_5 + masetero_dolor_izquierdo_1_5
  datos_procesados = datos_procesados + masetero_dolor_familiar_izquierdo_1_5 + ATM_dolor_izquierdo_1_5 + ATM_dolor_familiar_izquierdo_1_5
  datos_procesados = datos_procesados + otros_Musc_M_dolor_izquierdo_1_5 + otros_Musc_M_dolor_familiar_izquierdo_1_5 + no_Masticat_dolor_izquierdo_1_5
  datos_procesados = datos_procesados + no_Masticat_dolor_familiar_izquierdo_1_5 + temporal_dolor_izquierdo_2_5 + temporal_dolor_familiar_izquierdo_2_5
  datos_procesados = datos_procesados + temporal_cefalea_familiar_izquierdo_2_5 + masetero_dolor_izquierdo_2_5 + masetero_dolor_familiar_izquierdo_2_5
  datos_procesados = datos_procesados + ATM_dolor_izquierdo_2_5 + ATM_dolor_familiar_izquierdo_2_5 + otros_Musc_M_dolor_izquierdo_2_5
  datos_procesados = datos_procesados + otros_Musc_M_dolor_familiar_izquierdo_2_5 + no_Masticat_dolor_izquierdo_2_5 + no_Masticat_dolor_familiar_izquierdo_2_5
  datos_procesados = datos_procesados + temporal_dolor_izquierdo_3_5 + temporal_dolor_familiar_izquierdo_3_5 + temporal_cefalea_familiar_izquierdo_3_5
  datos_procesados = datos_procesados + masetero_dolor_izquierdo_3_5 + masetero_dolor_familiar_izquierdo_3_5 + ATM_dolor_izquierdo_3_5
  datos_procesados = datos_procesados + ATM_dolor_familiar_izquierdo_3_5 + otros_Musc_M_dolor_izquierdo_3_5 + otros_Musc_M_dolor_familiar_izquierdo_3_5
  datos_procesados = datos_procesados + no_Masticat_dolor_izquierdo_3_5 + no_Masticat_dolor_familiar_izquierdo_3_5

  datos_procesados = datos_procesados + click_apertura_derecho_6 + click_cierre_derecho_6 + click_paciente_derecho_6 + click_dolor_derecho_6 
  datos_procesados = datos_procesados + click_dolor_familiar_derecho_6 + crepitacion_apertura_derecho_6 + crepitacion_cierre_derecho_6 
  datos_procesados = datos_procesados + crepitacion_paciente_derecho_6 + click_apertura_izquierdo_6 + click_cierre_izquierdo_6 
  datos_procesados = datos_procesados + click_paciente_izquierdo_6 + click_dolor_izquierdo_6 + click_dolor_familiar_izquierdo_6 
  datos_procesados = datos_procesados + crepitacion_apertura_izquierdo_6 + crepitacion_cierre_izquierdo_6 + crepitacion_paciente_izquierdo_6 

  datos_procesados = datos_procesados + click_examinador_derecho_7 + click_paciente_derecho_7 + click_dolor_derecho_7 
  datos_procesados = datos_procesados + click_dolor_familiar_derecho_7 + crepitacion_examinador_derecho_7 + crepitacion_paciente_derecho_7 
  datos_procesados = datos_procesados + click_examinador_izquierdo_7 + click_paciente_izquierdo_7 + click_dolor_izquierdo_7 
  datos_procesados = datos_procesados + click_dolor_familiar_izquierdo_7 + crepitacion_examinador_izquierdo_7 + crepitacion_paciente_izquierdo_7 
  
  
  datos_procesados = datos_procesados + mientras_abre_bloqueo_derecho_8 + mientras_abre_paciente_derecho_8 + mientras_abre_evaluador_derecho_8
  datos_procesados = datos_procesados + posicion_max_apertura_bloqueo_derecho_8 + posicion_max_apertura_paciente_derecho_8 + posicion_max_apertura_evaluador_derecho_8
  datos_procesados = datos_procesados + mientras_abre_bloqueo_izquierdo_8 + mientras_abre_paciente_izquierdo_8 + mientras_abre_evaluador_izquierdo_8
  datos_procesados = datos_procesados + posicion_max_apertura_bloqueo_izquierdo_8 + posicion_max_apertura_paciente_izquierdo_8 + posicion_max_apertura_evaluador_izquierdo_8


  datos_procesados = datos_procesados + posterior_dolor_derecho_9 + posterior_dolor_familiar_derecho_9 + posterior_cefalea_familiar_derecho_9
  datos_procesados = datos_procesados + posterior_dolor_referido_derecho_9 + medio_dolor_derecho_9 + medio_dolor_familiar_derecho_9
  datos_procesados = datos_procesados + medio_cefalea_familiar_derecho_9 + medio_dolor_referido_derecho_9 + anterior_dolor_derecho_9
  datos_procesados = datos_procesados + anterior_dolor_familiar_derecho_9 + anterior_cefalea_familiar_derecho_9 + anterior_dolor_referido_derecho_9
  datos_procesados = datos_procesados + origen_dolor_derecho_9 + origen_dolor_familiar_derecho_9 + origen_dolor_referido_derecho_9
  datos_procesados = datos_procesados + cuerpo_dolor_derecho_9 + cuerpo_dolor_familiar_derecho_9 + cuerpo_dolor_referido_derecho_9
  datos_procesados = datos_procesados + insercion_dolor_derecho_9 + insercion_dolor_familiar_derecho_9 + insercion_dolor_referido_derecho_9
  datos_procesados = datos_procesados + lateral_dolor_derecho_9 + lateral_dolor_familiar_derecho_9 + lateral_dolor_referido_derecho_9
  datos_procesados = datos_procesados + alrededor_dolor_derecho_9 + alrededor_dolor_familiar_derecho_9 + alrededor_dolor_referido_derecho_9
  datos_procesados = datos_procesados + posterior_dolor_izquierdo_9 + posterior_dolor_familiar_izquierdo_9 + posterior_cefalea_familiar_izquierdo_9
  datos_procesados = datos_procesados + posterior_dolor_referido_izquierdo_9 + medio_dolor_izquierdo_9 + medio_dolor_familiar_izquierdo_9
  datos_procesados = datos_procesados + medio_cefalea_familiar_izquierdo_9 + medio_dolor_referido_izquierdo_9 + anterior_dolor_izquierdo_9
  datos_procesados = datos_procesados + anterior_dolor_familiar_izquierdo_9 + anterior_cefalea_familiar_izquierdo_9 + anterior_dolor_referido_izquierdo_9
  datos_procesados = datos_procesados + origen_dolor_izquierdo_9 + origen_dolor_familiar_izquierdo_9 + origen_dolor_referido_izquierdo_9
  datos_procesados = datos_procesados + cuerpo_dolor_izquierdo_9 + cuerpo_dolor_familiar_izquierdo_9 + cuerpo_dolor_referido_izquierdo_9
  datos_procesados = datos_procesados + insercion_dolor_izquierdo_9 + insercion_dolor_familiar_izquierdo_9 + insercion_dolor_referido_izquierdo_9
  datos_procesados = datos_procesados + lateral_dolor_izquierdo_9 + lateral_dolor_familiar_izquierdo_9 + lateral_dolor_referido_izquierdo_9
  datos_procesados = datos_procesados + alrededor_dolor_izquierdo_9 + alrededor_dolor_familiar_izquierdo_9 + alrededor_dolor_referido_izquierdo_9


  datos_procesados = datos_procesados + mandibular_dolor_derecho_10 + mandibular_dolor_familiar_derecho_10 + mandibular_dolor_referido_derecho_10
  datos_procesados = datos_procesados + submandibular_dolor_derecho_10 + submandibular_dolor_familiar_derecho_10 + submandibular_dolor_referido_derecho_10
  datos_procesados = datos_procesados + lateral_dolor_derecho_10 + lateral_dolor_familiar_derecho_10 + lateral_dolor_referido_derecho_10
  datos_procesados = datos_procesados + temporal_dolor_derecho_10 + temporal_dolor_familiar_derecho_10 + temporal_dolor_referido_derecho_10
  datos_procesados = datos_procesados + mandibular_dolor_izquierdo_10 + mandibular_dolor_familiar_izquierdo_10 + mandibular_dolor_referido_izquierdo_10
  datos_procesados = datos_procesados + submandibular_dolor_izquierdo_10 + submandibular_dolor_familiar_izquierdo_10 + submandibular_dolor_referido_izquierdo_10
  datos_procesados = datos_procesados + lateral_dolor_izquierdo_10 + lateral_dolor_familiar_izquierdo_10 + lateral_dolor_referido_izquierdo_10
  datos_procesados = datos_procesados + temporal_dolor_izquierdo_10 + temporal_dolor_familiar_izquierdo_10 + temporal_dolor_referido_izquierdo_10

  return datos_procesados