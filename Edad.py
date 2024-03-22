#DETERMINAR EDAD
from datetime import date, timedelta

def obtener_fecha_actual():
  return date.today()


def calcular_edad(fecha_nacimiento):
  fecha_actual = obtener_fecha_actual()
  
  
  if fecha_actual.month < fecha_nacimiento.month or (fecha_actual.month == fecha_nacimiento.month and fecha_actual.day <= fecha_nacimiento.day):
    edad = fecha_actual.year - fecha_nacimiento.year - 1
  else:
    edad = fecha_actual.year - fecha_nacimiento.year
  return edad

#SPLIT SE USA PARA DIVIDIR CADENAS
fecha_nacimiento_str = input("Ingrese su fecha de nacimiento (formato AÑO-MES-DIA): ")
fecha_nacimiento = date(*map(int, fecha_nacimiento_str.split('-')))


edad = calcular_edad(fecha_nacimiento)


print("Su edad es de", edad , "años.")