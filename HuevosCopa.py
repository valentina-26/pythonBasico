import math

pequeño = 47
grande = 67

RHO = 1.038
C = 3.7
K = 5.4 * 10 ** (-3)
TW = 100

big = input("El huevo es grande (si/No): ")

if (big == "si"):
    G = grande
    TemHue = float(input("por favor ingrese la temperatura original del huevo en °C: "))
    temp = (G**(2/3) * C * RHO**(1/3)) / (K * 3.1416**2) * (4 * 3.1416 / 3)**(2/3) * math.log(0.76 * (TemHue - TW) / (70 - TW))
    
else:
    P = pequeño
    TemHue = float(input("por favor ingrese la temperatura original del huevo en °C: "))
    Temp = (P**(2/3) * C * RHO**(1/3)) / (K * 3.1416**2) * (4 * 3.1416 / 3)**(2/3) * math.log(0.76 * (TemHue - TW) / (70 - TW))
    
print("El tiempo necesario para preparar el huevo a la copa es de aproximadamente {Temp:.2f} segundos.")    
