milista=[1,2,3,4,5,6]
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