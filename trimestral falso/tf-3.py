cifras=int(input("introduce el numero de cifras: "))
numero=int(input("introduce un numero: "))
multiplicar=0
contadopares=0
longitud=len(str(numero))

if longitud==cifras:
    for x in str(numero):
        multiplicar=multiplicar * int(x)
        if int(x)%2==0:
            contadopares +=1
else:
    print("longitud no correcta")

print(multiplicar)
