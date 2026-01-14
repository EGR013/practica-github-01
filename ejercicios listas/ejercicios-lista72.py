#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista
again=1
lista=[]
excepciones=("áéíóú")
correctas=("aeiou")
while again==1:
    b=input("introduce una letra: ")
    if b.isalpha:
        if b in excepciones:
            vocal = excepciones.find(b)
            b = correctas[vocal]
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