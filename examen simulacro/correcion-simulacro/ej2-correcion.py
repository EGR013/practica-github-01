import math
letra=input("elije el tipo de letra mayuscula(M) o minuscula(m):")
radio=int(input("introduce un radio: "))
altura=int(input("introduce una altura: "))

formula=round(((math.pi*radio**2)*altura),3)

print("el volumen es: ",formula)
if letra not in ("Mn"):
    print("error")
if letra=="M":
    print("EL VOLUMEN ES: ",formula)
else:
        print("el volumen es: ",formula)

          
