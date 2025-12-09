#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor
import math
forever=1
par=0
inpar=0
suma=0
negativo=0
positivo=0
lastnum=0
minimun=range(0,+math.inf)
max=range(0,-math.inf)
while forever==1:
    num=int(input("introduce un numero: "))
    if num==-99:
        break
    if num>0:
        positivo=positivo+1
    if num<0:
        negativo=negativo+1
    if num%2==0:
        par=par+1
    else:
        inpar=inpar+1
    if num<minimun:
        minimun=num
    if num>max:
        max=num
    suma=suma+num
print("RESUMEN")
print("El número de pares es: ",par) 
print("El número de impares es: ",inpar) 
print("El número de positivos es: ",positivo) 
print("El número de negativos es: ",negativo) 
print("El total es: ",suma)
print("el numero mas grande: ",max)
print("el numero mas pequeño: ",minimun)