frase=input("introduce una frase: ")
numero1=float(input("introduce un numero1"))
numero2=float(input("introduce un numero2"))
numero3=float(input("introduce un numero3"))

#apartado1

frase=frase.lower()

#apartado2
totalsuma=numero1+numero2+numero3
totalmedia=round(totalsuma/3,2)
totalproducto=numero1*numero2*numero3
print("la suma es:",totalsuma)
print("la media es:",totalmedia)
print("el producto es:",totalproducto)
if totalsuma>totalproducto:
    print("la suma es mayor que el producto")
if totalsuma<totalproducto:
    print("la suma no es mayor que el producto")