milista=[1,2,3,4,5,6]
milistacopiada=milista
print(milistacopiada)
milista.append("3")
milistapor2=[]
maximo=max(milista)
minimo=min(milista)
suma=sum(milista)
wop=0
print(milista)
print("maximo:",maximo)
print("minimo:")
print("suma tota: ",suma)

for x in range(len(milista)):
    calculo=milista[x]* 2
    milistapor2.append(calculo)
print(milistapor2)

for x in milista:
    milistapor2.append(x*2)

print(milistapor2)
milistapro=[n*2 for n in milista]

print(milistapro)