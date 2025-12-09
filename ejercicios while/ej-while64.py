#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:a) total de paresb) total de imparesc) total de números positivosd) total de números negativose) total de cerosf) total de la suma de todos los números introducidos
forever=1
par=0
inpar=0
suma=0
negativo=0
positivo=0
while forever==1:
    num=int(input("introduce un numero: "))
    if num==-99:
        break
    if num>0:
        positivo=positivo+1
    if num<0:
        negativo=negativo+1
    if num%2==0:
        par=par+1
    else:
        inpar=inpar+1
    suma=suma+num
print("RESUMEN")
print("El número de pares es: ",par) 
print("El número de impares es: ",inpar) 
print("El número de positivos es: ",positivo) 
print("El número de negativos es: ",negativo) 
print("El total es: ",suma)
