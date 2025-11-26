concatenar=""
inicio=int(input("introduce inicio: "))
fin=int(input("introduce final: "))
incremento=int(input("introduce incremento: "))
for x in range(inicio,fin,incremento):
    if not X%4==0:
         if x%6==0:
             concatenar=concatenar + "*" + str(x) + "*" + ","
        else:
            concatenar=concatenar + str(x) + ","
print(concatenar[:-1])
print(concatenar)
