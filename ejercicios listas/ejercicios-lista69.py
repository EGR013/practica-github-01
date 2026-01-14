#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.
a=int(input("quantos numeros quieres poner: "))
lista=[]
max=0
listafinal=[]
#set ordena de mayor a menor i elimina los repetidos
for x in range(0,a):
    b=int(input("introduce un numero de tu lista: "))
    lista.append(b)

lista.sort()
print(lista)