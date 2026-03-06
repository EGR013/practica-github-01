#El usuario introduce una serie de valores separados por comas en una única línea.
#Ejemplo de entrada:
#10,5,8,12,0,15,5,8
#El programa deberá:
#1. Convertir los valores en una lista numérica.
#2. Mostrar la lista original.
#3. Eliminar una única vez la puntuación más alta y la más baja.
#4. Mostrar la nueva lista resultante.
#5. Calcular la media de las puntuaciones restantes (redondeada a 2 decimales).
#6. Clasificar el rendimiento según la media obtenida:
 #- Menor que 5 → Rendimiento bajo
 #- Entre 5 y 10 → Rendimiento medio
 #- Mayor que 10 → Rendimiento alto

up=0
low=999**999
entrada=input("introduce una serie de valores seguidos por comas en una unica linea: ")
entrada=list(entrada.split(","))
print(entrada)
for x in entrada:
    if int(int(entrada[int(x)])>up):
        up=int(entrada[int(x)])
    if int(entrada[int(x)]<low):
        low=int(entrada[int(x)])
entrada.remove(up)
entrada.remove(low)
print(entrada)