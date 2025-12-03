#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos.
import random
intentos=0
numero=random.randint(0,1000)
motor=1
while motor==1:
    intentos=intentos+1
    num=int(input("Introduce un valor comprendido entre 1 y 1000: "))
    if num>numero:
        print("el numero es menor a el valor introducido")
    if num<numero:
        print("el numero es mayor a el valor introducido")
    if num==numero:
        motor=0
print("felicidades has adivinado el numero solo te ha tomado: ",intentos,"intentos!")

