#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra
import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
hit=1
digito=random.choice(lista)
while hit==1:
    print(lista)
    adivinacion=input("adivina la palabra escogida: ")
    if adivinacion==digito:
        print("muy bien lo has adivinado!")
        break
    else:
        print("incorrecto")
