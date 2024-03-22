#DETERMINAR TIPO DE TRIANGULO
def determinar_tipo_triangulo(a, b, c):

  if a == b and b == c:
    return "Equilátero"


  elif a == b or b == c or c == a:
    return "Isósceles"


  else:
    return "Escaleno"



a = float(input("Ingrese la longitud del primer lado del triángulo: "))
b = float(input("Ingrese la longitud del segundo lado del triángulo: "))
c = float(input("Ingrese la longitud del tercer lado del triángulo: "))

tipo_triangulo = determinar_tipo_triangulo(a, b, c)

print("El triángulo es" , tipo_triangulo)
