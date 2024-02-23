num1=int(input("ingrese el primer numero:"))
num2=int(input("ingrese el segundo numero:"))
num3=int(input("ingrese el tercer numero:"))

if int(num1)>int(num2) and int(num1)>int(num3):
    print ("el primer numero es mayor")

elif int(num2)>int(num1) and int(num2)>(num3):
    print("el segundo numero es mayor")

else:
    print("el tercer numero es mayor")