#CALCULADORA
num1 =float(input("por favor ingrese un numero: "))
num2=float(input("por favor ingrese otro numero: "))


suma=float(num1+num2)
resta=float(num1-num2)
multiplicacion=float(num1*num2)
division=float(num1/num2)

print("""     OPERACIONES DISPONIBLES
                1.suma
                2.resta
                3.multiplicacion
                4.division""")

opcion =float(input("que operacion desea realizar:"))



if opcion == 1:
    print("La suma es igual a: " , suma)
    
elif opcion == 2:
    print("La resta es igual a: " , resta)
    
elif opcion == 3:
    print("La multiplicacion es igual a: ", multiplicacion)
        
elif opcion == 4:
    print("La division es igual a: ", division)


opcion =float(input("que operacion desea realizar:"))



if opcion == 1:
    print("La suma es igual a: " , suma)
    
elif opcion == 2:
    print("La resta es igual a: " , resta)
    
elif opcion == 3:
    print("La multiplicacion es igual a: ", multiplicacion)
        
elif opcion == 4:
    print("La division es igual a: ", division)


