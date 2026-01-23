#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así sucesivamente.Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe algún método que permita sumar el contenido de una lista?
import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
hit=1
puntuacion=[]
digito=random.choice(lista)
points=8
jugadas=1
while hit==1:
    print(lista)
    adivinacion=input("adivina la palabra escogida: ")
    if adivinacion==digito:
        print("muy bien lo has adivinado!")
        puntuacion.append(points)
        elecion=input(int("quieres voler a jugar si(1) no(2): "))
        if elecion==1:
            points=points+8
            jugadas=jugadas+1
        else:
            break
    else:
        print("incorrecto")
        points=points-1

media=jugadas*4
print("tu puntuacion total a sido: ",sum(puntuacion))
total=sum(puntuacion)
print("ahora comprovare si tu puntuacion supera la media.....")
if total>media:
    print("tienes una suerte elevada porfavor apuesta con todo lo que te pertenence")
else:
    print("quizas es prudente que entres a un casino")
