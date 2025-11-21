#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
again=1
repeticiones=0
sumatotal=0
while again==1:
    num1=int(input("introduce un numero entero: "))
    num2=int(input("introduce otro numero entero: "))
    suma=num1+num2
    print(suma)
    print(sumatotal)
    repeticiones=repeticiones+1
    sumatotal=sumatotal+suma
    if sumatotal>50:
        print("has hecho: ",repeticiones,"repeticiones i la suma total es: ",sumatotal)
        break  
    else:
        continue