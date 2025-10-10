
frase=str(input("introduce una frase: "))
frase=str.lower(frase)
print(": ",frase)
num1=int(input("dame un numero "))
num2=int(input("dame otro numero "))
num3=int(input("ermm dame otro numero "))
suma=num1+num2+num3
media=suma/3
producto=num1*num2*num3
print("la suma es: ",suma)
print("la media es: ",media)
print("el producto es: ",producto)
if suma>producto:
    print("la suma es mayor que el producto")
if suma<producto:
    print("la suma no es mayor que el producto")
