Not1 = int(input("por favor ingrese la primera nota: "))
Not2 = int(input("por favor ingrese la segunda nota: "))
Lab = float(input("por favor ingrese la nota del laboratorio: "))

Nc = (60-(Lab * 0.3))
divion = Nc / 0.7

Not3 = 3 * divion - Not1 - Not2

print("la nota que necesitas para aprobar el ramo con nota final 60 es:" ,Not3 ,)