from django import forms

def mientras_abre_bloqueo_derecho_8():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Mientras Abre Bloqueo"
	)
def mientras_abre_paciente_derecho_8():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Mientras Abre Paciente"
	) 
def mientras_abre_evaluador_derecho_8(): 
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Mientras Abre Evaluador"
	)
def posicion_max_apertura_bloqueo_derecho_8():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Posicion Max Apertura Bloqueo"
	) 
def posicion_max_apertura_paciente_derecho_8():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Posicion Max Apertura Paciente"
	)
def posicion_max_apertura_evaluador_derecho_8():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Posicion Max Apertura Evaluador"
	)

def mientras_abre_bloqueo_izquierdo_8():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Mientras Abre Bloqueo"
	)
def mientras_abre_paciente_izquierdo_8():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Mientras Abre Paciente"
	) 
def mientras_abre_evaluador_izquierdo_8(): 
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Mientras Abre Evaluador"
	)
def posicion_max_apertura_bloqueo_izquierdo_8():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Posicion Max Apertura Bloqueo"
	) 
def posicion_max_apertura_paciente_izquierdo_8():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Posicion Max Apertura Paciente"
	)
def posicion_max_apertura_evaluador_izquierdo_8():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Posicion Max Apertura Evaluador"
	)