#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.
again=1
lista=[]
while again==1:
    b=input("introduce una letra: ")
    if b.isalpha:
        lista.append(b)
        answear=int(input("quieres seguir , no(1),si(2) (introduce el numero no la palabra: )"))
        if answear==1:
            again=again+420
        else:
            print("continuaremos con la lista")
    else:
        print("esto no es una letra pruebalo otra vez")
lista=list(set(lista))
print(lista)