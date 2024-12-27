from django import forms

def patron_apertura():
	return forms.ChoiceField(
		choices=[
			('recto', 'Recto'), 
			('corregida', 'Desviación corregida'), 
			('ncorregida', 'Desviación no corregida')
		],
		widget=forms.RadioSelect(),
		label="Patron de apertura"
	)

def lado_apertura():
	return forms.ChoiceField(
		choices=[
			('derecha', 'Derecha'), 
			('izquierda', 'Izquierda'), 
			('ninguno', 'Ninguno')
		],
		widget=forms.RadioSelect(),
		label="Lado de apertura"
	)