from django import forms

def localizacion_dolor_derecho():
	return forms.MultipleChoiceField(
		choices=[
			('N', 'Ninguno'), 
			('T', 'Temporal'), 
			('M', 'Masetero'), 
			('A', 'ATM'), 
			('O', 'Otros musc masticatorios'), 
			('E', 'Estructura No-masticatoria')
		],
		widget=forms.CheckboxSelectMultiple(),
		label="LADO DERECHO"
	)
	
def localizacion_dolor_izquierdo():
	return forms.MultipleChoiceField(
		choices=[
			('N', 'Ninguno'), 
			('T', 'Temporal'), 
			('M', 'Masetero'), 
			('A', 'ATM'), 
			('O', 'Otros musc masticatorios'), 
			('E', 'Estructura No-masticatoria')
		],
		widget=forms.CheckboxSelectMultiple(),
		label="LADO IZQUIERDO"
	)

def localizacion_cefalea_derecho():
	return forms.MultipleChoiceField(
		choices=[
			('N', 'Ninguno'), 
			('T', 'Temporal'), 
			('O', 'Otro')
		],
		widget=forms.CheckboxSelectMultiple(),
		label="LADO DERECHO"
	)

def localizacion_cefalea_izquierdo():
	return forms.MultipleChoiceField(
		choices=[
			('N', 'Ninguno'), 
			('T', 'Temporal'), 
			('O', 'Otro')
		],
		widget=forms.CheckboxSelectMultiple(),
		label="LADO IZQUIERDO"
	)