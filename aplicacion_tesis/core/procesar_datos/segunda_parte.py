def convertir_segunda_parte(cleaned_data_1,cleaned_data_2):
  response = []
  if cleaned_data_2 == "D":
    response = [cleaned_data_1,0]
  elif cleaned_data_2 == "I":
    response = [0,cleaned_data_1]
  elif cleaned_data_2 == "N":
    response = [0,0]
  return response
