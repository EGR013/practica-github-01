#for x in range
#for j in

#while condicion:
#ej1
i=1
while i<10:
    print("hola" + str(i))
    i+=1
#ej2
edad=int(input("introduce la edad"))
while edad>1000:
    print("edad incorrecta:")
    edad=int(input("vuelve a introducir tu edad: "))
    if edad==999:
        break
print("fin programa")
#ejercicio
attempt=0
import random
num=int(input("introduce un numero del 1 al 20"))
while attempt<4:
    numat=int(input("adivina el numero secreto"))
    if numat==num:
        print("muy bien lo has adivinado")
if numat>num or numat<num:
    print("numero incorrecto")
    attempt=attempt+1
#ejercicio(correcion(?))
while num==numat:
    if numat>0 and numat<=20:
    #num=random.randit(1,20)
        print(f"has introducido el numero {numat} no has accertado")
    else:
        print("rango incorrecto")
        