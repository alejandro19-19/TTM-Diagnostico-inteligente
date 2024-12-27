def convertir_primera_parte_a(cleaned_data):
  response = ["No","No","No","No","No","No"]
  for i in cleaned_data:
    if i == "N":
      response[0] = "Si"
    elif i == "M":
      response[1] = "Si"
    elif i == "T":
      response[2] = "Si"
    elif i == "A":
      response[3] = "Si"
    elif i == "O":
      response[4] = "Si"
    elif i == "E":
      response[5] = "Si"
  return response

def convertir_primera_parte_b(cleaned_data):
  response = ["No","No","No"]
  for i in cleaned_data:
    if i == "N":
      response[0] = "Si"
    elif i == "T":
      response[1] = "Si"
    elif i == "O":
      response[2] = "Si"
  return response
