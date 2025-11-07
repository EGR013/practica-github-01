#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario
numero=int(input("dime el numero de numeros naturales: "))
numeroisnumero=numero
suma=0
for x in range(numero):
    suma=suma+numeroisnumero
    numeroisnumero=numeroisnumero-1
print("el resultado de la suma es: ",suma)
