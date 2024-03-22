#DETERMINAR GANADOR
def determinar_ganador_set(m, n):


  if m < 0 or n < 0:
    return "Invalido"

 #gana A 
  if m >= 6 and m - n >= 2:
    return "A"

#gana B
  elif n >= 6 and n - m >= 2:
    return "B"

#empatado
  if m == 5 and n == 5:
    return "Continua"

#ultimo set
  if m == 6 and n == 6:
    return "Continua"


  return "Invalido"


m = int(input("Ingrese el número de juegos ganados por el jugador A: "))
n = int(input("Ingrese el número de juegos ganados por el jugador B: "))

resultado = determinar_ganador_set(m, n)

if resultado == "A":
  print("El jugador A gano el set.")
  
elif resultado == "B":
  print("El jugador B gano el set.")
  
elif resultado == "Continua":
  print("El set todavia no ha terminado.")
  
else:
  print("El resultado es inválido.")


      
