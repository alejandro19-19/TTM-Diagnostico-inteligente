from django import forms

def apertura_sin_dolor():
  return forms.IntegerField(
        label="A. Apertura Sin Dolor (mm)",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 3'})
    )
	
def	apertura_maxima_no_asistida():
  return forms.IntegerField(
        label="B. Apertura Maxima No Asistida (mm)",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 3'})
    )
	
def	apertura_Maxima_Asistida():
  return forms.IntegerField(
        label="C. Apertura Maxima Asistida (mm)",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 3'})
    )

def	terminada():
  return forms.ChoiceField(
		choices=[
			('Si', 'Si'), 
			('No', 'No')
		],
		widget=forms.RadioSelect(),
		label="¿Terminada?"
	)

def temporal_dolor_derecho_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor"
	)
def	temporal_dolor_familiar_derecho_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor Familiar"
	)
def	temporal_cefalea_familiar_derecho_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Cefalea Familiar"
	)
	
def	masetero_dolor_derecho_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	masetero_dolor_familiar_derecho_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	ATM_dolor_derecho_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	ATM_dolor_familiar_derecho_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	otros_Musc_M_dolor_derecho_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	otros_Musc_M_dolor_familiar_derecho_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	no_Masticat_dolor_derecho_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	no_Masticat_dolor_familiar_derecho_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	temporal_dolor_derecho_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor"
	)
def	temporal_dolor_familiar_derecho_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor Familiar"
	)
def	temporal_cefalea_familiar_derecho_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Cefalea Familiar"
	)
	
def	masetero_dolor_derecho_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	masetero_dolor_familiar_derecho_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	ATM_dolor_derecho_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	ATM_dolor_familiar_derecho_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	otros_Musc_M_dolor_derecho_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	otros_Musc_M_dolor_familiar_derecho_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	no_Masticat_dolor_derecho_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	no_Masticat_dolor_familiar_derecho_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	temporal_dolor_izquierdo_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor"
	)
def	temporal_dolor_familiar_izquierdo_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor Familiar"
	)
def	temporal_cefalea_familiar_izquierdo_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Cefalea Familiar"
	)
	
def	masetero_dolor_izquierdo_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	masetero_dolor_familiar_izquierdo_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	ATM_dolor_izquierdo_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	ATM_dolor_familiar_izquierdo_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	otros_Musc_M_dolor_izquierdo_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	otros_Musc_M_dolor_familiar_izquierdo_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	no_Masticat_dolor_izquierdo_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	no_Masticat_dolor_familiar_izquierdo_1_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	temporal_dolor_izquierdo_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor"
	)
def	temporal_dolor_familiar_izquierdo_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor Familiar"
	)
def	temporal_cefalea_familiar_izquierdo_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Cefalea Familiar"
	)
	
def	masetero_dolor_izquierdo_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	masetero_dolor_familiar_izquierdo_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	ATM_dolor_izquierdo_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	ATM_dolor_familiar_izquierdo_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	otros_Musc_M_dolor_izquierdo_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	otros_Musc_M_dolor_familiar_izquierdo_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	no_Masticat_dolor_izquierdo_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	no_Masticat_dolor_familiar_izquierdo_2_4():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)