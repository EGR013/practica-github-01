#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While
again=1
repeticiones=0
sumatotal=0
while again==1:
    num1=int(input("introduce un numero entero: "))
    num2=int(input("introduce otro numero entero: "))
    suma=num1+num2
    print(suma)
    repeticiones=repeticiones+1
    sumatotal=sumatotal+suma
    choice=int(input("quieres repetir la operacion si(1) o no(2)?: "))
    if choice==2:
        print("has heco: ",repeticiones,"repeticiones i la suma total es: ",sumatotal)
        break  
    else:
        continue