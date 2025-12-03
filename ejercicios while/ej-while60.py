#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. Utiliza únicamente el while
tablaselec=1
tablahit=0
num=int(input("introduce un numero: "))
while tablaselec<11:
    tablahit=tablaselec*num
    print(tablahit)
    tablaselec=tablaselec+1