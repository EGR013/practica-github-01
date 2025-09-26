#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
radio=int(input("introduce el radio de un cilindro "))
altura=int(input("introduce la altura de un cilindro "))
volumen=math.pi*(radio**2)*altura
area=2*math.pi*radio*(radio+altura)
volumen=round(volumen,2)
area=round(area,2)
print("el area de el cilindro es ",area)
print("el volumen de el cilindro es ",volumen)
