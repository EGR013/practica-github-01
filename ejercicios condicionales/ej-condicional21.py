#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
Ax=float(input("introduce el numero a "))
Bx=float(input("introduce el numero b "))
Cx=float(input("introduce el numero c "))
X=(Bx**2)-(4*Bx*Cx)
Raiz=math.sqrt(X)
if X<0:
    print("la raiz no puede ser negativa")
x1=(-1*Bx)+Raiz/(2*Ax)
x2=(-1*Bx)-Raiz/(2*Ax)
print("el valor de x1 es ",x1)
print("el valor de x2 es ",x2)
