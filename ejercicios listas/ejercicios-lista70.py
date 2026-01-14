#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.
lista1=[]
lista2=[]
lon=int(input("introduce el numero de palabras que quieres introducir: "))
for x in range(0,lon):
    a=input("introduce una palabra: ")
    lista1.append(a)
lista1.sort()
print("la primera lista contiene: ",lista1)
lista1.reverse()
print("la segunda lista contiene: ",lista1)