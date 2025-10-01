#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
Ax=int(input("introduce el numero a "))
Bx=int(input("introduce el numero b "))
Cx=int(input("introduce el numero c "))
X=(Bx**2)-(4*Bx*Cx)
Raiz=math.sqrt(X)
if Raiz<0:
    print("la raiz no puede ser negativa")
x1=(-Bx+Raiz)/2*Ax
x2=(-Bx-Raiz)/2*Ax
print("el valor de x1 es ",x1)
print("el valor de x2 es ",x2)
