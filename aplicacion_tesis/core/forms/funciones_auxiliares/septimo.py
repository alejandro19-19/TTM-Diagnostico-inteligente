from django import forms

def	click_examinador_derecho_7(): 
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Click Examinador"
	)
def click_paciente_derecho_7(): 
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Click paciente"
	) 
def click_dolor_derecho_7():  
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Click Dolor"
	)
def click_dolor_familiar_derecho_7(): 
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Click Dolor Familiar"
	) 
def crepitacion_examinador_derecho_7():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Crepitacion Examinador"
	) 
def crepitacion_paciente_derecho_7(): 
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Crepitacion Paciente"
	)
def click_examinador_izquierdo_7(): 
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Click Examinador"
	)
def click_paciente_izquierdo_7():  
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Click Paciente"
	)
def click_dolor_izquierdo_7(): 
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Click Dolor"
	) 
def click_dolor_familiar_izquierdo_7():  
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Click Dolor Familiar"
	)
def crepitacion_examinador_izquierdo_7(): 
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Crepitacion Examinador"
	)
def crepitacion_paciente_izquierdo_7():   
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Crepitacion Paciente"
	)