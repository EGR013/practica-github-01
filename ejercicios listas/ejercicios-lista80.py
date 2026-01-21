#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.
numero=list(input("introduce un numero: "))
length=len(numero)
point=0
for i in range(0,length):
    if "." in i:
        point=point+1
    if str(i).isalpha():
        point=2

if point==1:
    print("es un numero con decimales")
else:
    print("no es un numero con decimales")

        
