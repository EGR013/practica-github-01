#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
num1=int(input("introduce un numero: "))
num2=int(input("introduce otro numero: "))
if num1<num2:
    for i in range(num1,num2):
if num1>num2:
    for i in range(num2,num1):
if num1==num2:
    for i in range(num1,num2)