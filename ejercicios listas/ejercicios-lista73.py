#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
place=0
errors=[]
okay=[]
for i in lista1:
    if i in lista2:
        errors.append(i)  
    else:
        okay.append(i)

print("estan repetidas: ",errors)
print("no estan repetidas: ",okay)

    

