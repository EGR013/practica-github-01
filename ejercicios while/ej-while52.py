#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
again=1
while again==1:
    num1=int(input("introduce un numero entero: "))
    num2=int(input("introduce otro numero entero: "))
    suma=num1+num2
    print(suma)
    choice=int(input("quieres repetir la operacion si(1) o no(2)?: "))
    if choice==2:
        break
    else:
        continue