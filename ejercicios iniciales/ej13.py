#13. Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el área y para calcular el volumen utiliza el operador de exponente.
lado=int(input("introduce el lado de un cubo "))
area=(lado*lado)*6
volumen=(lado**3)
print("el area es ",area)
print("el volumen es ",volumen)