#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
num1=int(input("introduce un numero: "))
num2=int(input("introduce otro numero: "))
num3=num1
num4=num2
par=""
inpar=""
if num1<num2:
    for i in range(num1,num2):
        if num3%2==0:       
            par=(num3,"-")+par
        else:
            inpar=(num3,"-")+inpar
        num3=num3+1
if num1>num2:
    for i in range(num2,num1):
        if num4%2==0:
            par=(num4,"-")+par
        else:
            inpar=(num4,"-")+inpar
        num4=num4+1
if num1==num2:
    for i in range(num1,num2):
        if num3%2==0:       
            par=(num3,"-")+par
        else:
            inpar=(num3,"-")+inpar
        num3=num3+1
print("los numeros pares son: ",par)
print("los numeros inpares son: ",inpar)