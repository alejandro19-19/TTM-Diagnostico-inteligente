from django import forms

def lateralidad_derecha():
  return forms.IntegerField(
        label="A. Lateralidad Derecha (mm)",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 3'})
    )
	
def	lateralidad_izquierda():
  return forms.IntegerField(
        label="B. Lateralidad Izquierda (mm)",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 3'})
    )
	
def protusion():
	return forms.IntegerField(
		label="C. Protrusión (mm)",
		widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 3'}),
	)

def temporal_dolor_derecho_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor"
	)
def	temporal_dolor_familiar_derecho_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor Familiar"
	)
def	temporal_cefalea_familiar_derecho_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Cefalea Familiar"
	)
	
def	masetero_dolor_derecho_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	masetero_dolor_familiar_derecho_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	ATM_dolor_derecho_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	ATM_dolor_familiar_derecho_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	otros_Musc_M_dolor_derecho_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	otros_Musc_M_dolor_familiar_derecho_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	no_Masticat_dolor_derecho_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	no_Masticat_dolor_familiar_derecho_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	temporal_dolor_derecho_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor"
	)
def	temporal_dolor_familiar_derecho_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor Familiar"
	)
def	temporal_cefalea_familiar_derecho_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Cefalea Familiar"
	)
	
def	masetero_dolor_derecho_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	masetero_dolor_familiar_derecho_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	ATM_dolor_derecho_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	ATM_dolor_familiar_derecho_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	otros_Musc_M_dolor_derecho_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	otros_Musc_M_dolor_familiar_derecho_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	no_Masticat_dolor_derecho_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	no_Masticat_dolor_familiar_derecho_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	temporal_dolor_derecho_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor"
	)
def	temporal_dolor_familiar_derecho_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor Familiar"
	)
def	temporal_cefalea_familiar_derecho_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Cefalea Familiar"
	)
	
def	masetero_dolor_derecho_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	masetero_dolor_familiar_derecho_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	ATM_dolor_derecho_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	ATM_dolor_familiar_derecho_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	otros_Musc_M_dolor_derecho_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	otros_Musc_M_dolor_familiar_derecho_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	no_Masticat_dolor_derecho_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	no_Masticat_dolor_familiar_derecho_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	temporal_dolor_izquierdo_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor"
	)
def	temporal_dolor_familiar_izquierdo_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor Familiar"
	)
def	temporal_cefalea_familiar_izquierdo_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Cefalea Familiar"
	)
	
def	masetero_dolor_izquierdo_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	masetero_dolor_familiar_izquierdo_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	ATM_dolor_izquierdo_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	ATM_dolor_familiar_izquierdo_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	otros_Musc_M_dolor_izquierdo_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	otros_Musc_M_dolor_familiar_izquierdo_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	no_Masticat_dolor_izquierdo_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	no_Masticat_dolor_familiar_izquierdo_1_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	temporal_dolor_izquierdo_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor"
	)
def	temporal_dolor_familiar_izquierdo_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor Familiar"
	)
def	temporal_cefalea_familiar_izquierdo_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Cefalea Familiar"
	)
	
def	masetero_dolor_izquierdo_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	masetero_dolor_familiar_izquierdo_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	ATM_dolor_izquierdo_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	ATM_dolor_familiar_izquierdo_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	otros_Musc_M_dolor_izquierdo_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	otros_Musc_M_dolor_familiar_izquierdo_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	no_Masticat_dolor_izquierdo_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	no_Masticat_dolor_familiar_izquierdo_2_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	temporal_dolor_izquierdo_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor"
	)
def	temporal_dolor_familiar_izquierdo_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Dolor Familiar"
	)
def	temporal_cefalea_familiar_izquierdo_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Temporal Cefalea Familiar"
	)
	
def	masetero_dolor_izquierdo_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	masetero_dolor_familiar_izquierdo_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	ATM_dolor_izquierdo_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	ATM_dolor_familiar_izquierdo_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	otros_Musc_M_dolor_izquierdo_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	otros_Musc_M_dolor_familiar_izquierdo_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)

def	no_Masticat_dolor_izquierdo_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor"
	)
def	no_Masticat_dolor_familiar_izquierdo_3_5():
  return forms.ChoiceField(
			choices=[('Si', 'Si'), ('No', 'No')],
			widget=forms.RadioSelect(),
			label="Masetero Dolor Familiar"
	)