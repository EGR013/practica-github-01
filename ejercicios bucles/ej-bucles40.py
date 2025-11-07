#40. Crea un programa que cuente todos los números pares hasta el número 50
numero=1
par=0
inpar=0
for i in range(1,51):
    if i%2==0:
        par=par+1
    else:
        inpar=inpar+1
    numero=numero+1

