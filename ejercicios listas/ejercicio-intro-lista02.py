#Ejercicio 2: Manipulación de cadenas con listas Escribe un programa que pida al usuario una cadena de texto y la convierta en una lista de palabras. Luego, realiza lo siguiente:
#Imprime la lista de palabras.
#Cuenta cuántas veces aparece una palabra específica (la que elija el usuario).
#Une la lista de palabras nuevamente en una cadena de texto separada por espacios.
listanumeros=[]
listanonumeros=[]
listatodo=[]

frase=input("introduce valores separados por un valor:")

listatodo=frase.split("-")

for x in range(len(listatodo)):
    if listatodo[x].isnumeric():
        listanumeros.append(int(listatodo[x]));
    else:
        listanumeros.append(listatodo[x])

print(listanumeros)

print(sum(listanumeros))