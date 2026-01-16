#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.
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

for x in lista2:
    if x in lista1:
        errors.append(x)  
    else:
        okay.append(x)

errors=list(set(errors))

print("estan repetidas: ",errors)
print("no estan repetidas: ",okay)