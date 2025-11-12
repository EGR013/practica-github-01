#43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra
palabra=str(input("introduce una palabra: "))
count=0
leter=""
pal_count=len(palabra)+1
for i in range(1,pal_count):
    part=palabra[count]
    print("en la posicion",count,"esta la letra: ",part)
    count=count+1

