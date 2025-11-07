#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.
repeticion=int(input("introduce el numero de numeros que quieres introducir: "))
negativo=0
positivo=0
cero=0
for i in range(1,repeticion+1):
    numero=float(input("introduce un numero: "))
    if numero<0:
        negativo=negativo+1
    if numero>0:
        positivo=positivo+1
    if numero==0:
        cero=cero+1
print("el numero de positivos es: ",positivo,"el numero de negativos es: ",negativo,"i el de ceros es: ",cero)