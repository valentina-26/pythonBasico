year = int(input("por fsavor ingrese un año"))

if year < 1582:
    if year % 4 == 0:
        print(year,"es un año bisiesto")
        
    else:
        print(year, "no es año bisiesto")
        
else:
    if ((year % 4 == 0) and (year% 100 != 0)) or year % 400 == 0: 
        print(f"{year} es año bisiesto.")
    else:
        print(f"{year} NO es año bisiesto.")
        