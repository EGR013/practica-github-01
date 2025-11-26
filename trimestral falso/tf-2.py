sumapositivos=0
sumanegativos=0
contadormayor=0


for x in range(7):
    numero=int(input("introduce el numero: "))
    if numero>0:
        sumapositivos=sumapositivos+numero
        if numero>100:
            contadormayor=contadormayor+1
    else:
        sumanegativos=sumanegativos+numero
print("suma de positivso:",sumapositivos)
print("suma negativos:",sumanegativos)