num = int(input("escriba el numero:"))
A = 1
B = 0
while n <= num:
    if num % n == 0:
        B = B + 1
    A = A + 1
    if B == 2:
        print ("si es primo")
    else:
        print("no es primo")