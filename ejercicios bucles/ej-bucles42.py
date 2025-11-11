#42. Imprima el siguiente patrón con el ciclo for.

#Inicializamos las variables
num_asteriscos = 1
num = 5
salida = ""
sube_baja = 1

#El primer bucle, en primer lugar, imprime la salida, que es determinada por el segundo bucle. 
#Después, le vuelve a dar a salida un valor en blanco para la siguiente vez que el segundo bucle la asigne. 
#El condicional comprueba si ya hemos llegado a 5 asteriscos o no. En este caso, empieza la bajada.
#Por último, suma al número de asteriscos que se imprimirán la siguiente vez 1 por sube_baja. 
for i in range(1, (2 * num)):
    for i in range(1, num_asteriscos + 1):
        #Este bucle asigna a la variable salida el nñumero de asteriscos que indica la variable num_asteriscos. 
        salida = salida + "*"
    print(salida)
    salida = ""
    if num_asteriscos >= num and sube_baja == 1:
        sube_baja = -1
    num_asteriscos += 1 * sube_baja