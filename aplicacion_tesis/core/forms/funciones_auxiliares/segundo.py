from django import forms

def diente_referencia(): 
  return forms.ChoiceField(
		choices=[
			('FDI#11', 'FDI # 11'), 
			('FDI#21', 'FDI # 21'), 
			('O', 'Otro')
		],
		widget=forms.RadioSelect(),
		label="Diente de Referencia"
	)

def sobre_mordida_horizontal():
  return forms.IntegerField(
    label="Sobre-mordida Horizontal (mm)",
    widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 3'})
  )
	
def sobre_mordida_vertical():
  return forms.IntegerField(
    label="Sobre-mordida vertical (mm)",
    widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 3'})
  )

def desviacion_linea_media():
  return forms.IntegerField(
    label="Desviacion linea media (mm)",
    widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 3'})
  )

def desviacion_linea_lado():
  return forms.ChoiceField(
  choices=[
    ('D', 'Derecho'),
    ('I', 'Izquierdo'), 
    ('N', 'Ninguno')
  ],
  widget=forms.RadioSelect(),
  label="Lado hacia el que está la desviación"
)