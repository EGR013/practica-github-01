
var1=int(input("introduce un numero: "))
var2=int(input("introduce otro numero: "))
total1=var1//var2
total2=var1%var2
print("el coeficiente es: ",total1)
print("el resto es: ",total2)
if var1%var2==0:
    print("el dividendo es par")
else:
    print("el dividendo es inpar")