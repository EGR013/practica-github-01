#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40.
tablaselec=1
tablahit=0
num=int(input("introduce un numero: "))
while tablaselec<11:
    tablahit=tablaselec*num
    print(tablahit)
    tablaselec=tablaselec+1
    if tablahit>40 or tablahit==40:
        break
print("fin de el programa")