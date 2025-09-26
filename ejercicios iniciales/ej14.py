#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal
import math
diametro=float(input("introduce el diametro de un circulo "))
radio=diametro/2
area=math.pi*(radio**2)
perimetro=math.pi*diametro
area=round(area,1)
perimetro=round(perimetro,1)
print("el area de el circulo es ",area)
print("el perimetro de el circulo es ",perimetro)