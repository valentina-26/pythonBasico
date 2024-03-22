# DETERMINAR SI UN CARACTER ES LETRA, NUMERO O NINGUNO

caracter = input("Por favor ingrese un caracter: ")
 
 
 # islower verifica si todos los caracteres en una cadena están en minúsculas 
if caracter.islower():
    print(caracter, "es una letra minuscula: ")
    
#isupper verifica si los caracteres estan en mayuscula.
elif caracter.isupper():
    print(caracter, "es una letra mayuscula: ")
    
#isdigit verifica si todos los caracteres  dígitos numéricos
elif caracter.isdigit():
    print(caracter, "es un numero: ")
    
else:
    print(caracter, "no es ni letra ni numero: ")    

        