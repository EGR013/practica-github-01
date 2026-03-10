variable="10,5,8,12,0,15,5,8"
variable=input("introduce valores: ")
lista=variable.split(",")
lista=[int(x) for x in lista]
print(lista)
valormaxi=max(lista)
valormin=min(lista)

lista.remove(valormaxi)
lista.remove(valormin)

valormedia=round(sum(lista)/len(lista),2)
print("La media es: ",valormedia)

print(lista)
if valormedia<5:
    print("rendimiento bajo")
if valormedia>=5 and valormedia<=10:
    print("rendimiento medio")
if valormedia>10:
    print("rendimiento alto")