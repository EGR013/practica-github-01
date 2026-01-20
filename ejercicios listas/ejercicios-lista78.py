#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
numericos=[]
mayus=0
letras=0
numeros=0
lista1=[" a","b","D","x","r","X","3","h","w","2","i"]
longitud=len(lista1)
for i in lista1:
    if i.isnumeric():
        numeros=int(numeros+1)
        numericos.append(int(i))
    if i.isalpha():
        letras=int(letras+1)
    if i.isupper():
        mayus=int(mayus+1)

suma=sum(numericos)
print("cantidad total de valores: ",longitud)
print("cantidad de numericos: ",numeros)
print("cantidad de letras: ",letras)
print("cantidad de mayusculas: ",mayus)
print("suma de los valors numericos: ",suma)

stay=1
while stay==1:
    choice=int(input("quieres eliminar un valor de la lista?: no(1) si(2): "))
    if choice==1:
        stay=stay+420
    else:
        choiceagain=input("introduce el valor que quieres eliminar: ")