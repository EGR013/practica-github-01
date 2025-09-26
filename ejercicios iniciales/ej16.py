#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división)
import math
numero=int(input("introduce un numero "))
raiz=math.sqrt(numero)
division=raiz//2
raiz=round(raiz,1)
print("la raiz cuadrada de este numero es ",raiz)
print("el resultado de la division es ",division)
