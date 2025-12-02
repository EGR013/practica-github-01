#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
numero=random.randit(1,5)
why=1
while why==1:
    num=int(input("introduce un numero entre el 1 i el 5 para adivinar el digito secreto: "))
    if num>0 or num<6:
        if num==numero:
            print("as adivinado el numero!!!!")
        else:
            print("numero incorrecto")
    else:
        print("digito incorrecto mantente en el rango")
    