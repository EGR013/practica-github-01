#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While
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
#incompleto actualmente