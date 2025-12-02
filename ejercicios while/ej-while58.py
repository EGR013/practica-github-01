#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
numero=random.randit(1,5)
attempts=3
while attempts>0:
    num=int(input("introduce un numero entre el 1 i el 5 para adivinar el digito secreto: "))
    if num>0 or num<6:
        if num==numero:
            print("as adivinado el numero!!!!")
        else:
            print("numero incorrecto")
            attempts=attempts-1
    else:
        print("digito incorrecto mantente en el rango")
        attempts=attempts-1
print("se te acabaron los intentos")