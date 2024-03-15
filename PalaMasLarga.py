word1 = input("por favor ingrese una palabra: ")
word2 = input("por favor ingrese otra palabra: ")

lettersP1 = len(word1)
lettersP2 = len(word2)

resta1 = lettersP1-lettersP2
resta2 = lettersP2-lettersP1

if lettersP1 > (lettersP2):
    print("la primera palabra es mas larga por", resta1 , "letras")
    
else:
    print("la segunda palabra es mas larga por", resta2,"letras" )
