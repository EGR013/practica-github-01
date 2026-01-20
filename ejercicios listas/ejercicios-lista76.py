#76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
numericos=[]
lista2=[]
mayus=0
letras=0
numeros=0
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
longitud=len(lista1)
for i in lista1:
    if i.isnumeric():
        numeros=int(numeros+1)
        numericos.append(int(i))
    if i.isalpha():
        letras=int(letras+1)
        lista2.append(i)
    if i.isupper():
        mayus=int(mayus+1)

suma=sum(numericos)
print("cantidad total de valores: ",longitud)
print("cantidad de numericos: ",numeros)
print("cantidad de letras: ",letras)
print("cantidad de mayusculas: ",mayus)
print("suma de los valors numericos: ",suma)
choice=int(input(("ahora voy a mostrar la lista deseas verla en orden ascendente(1) o descendente(2): ")))

lista2.sort()
numericos.sort()
if choice==2:
    lista2.reverse()
    numericos.reverse
    print(numericos)
    print(lista2)
else:
    print(numericos)    
    print(lista2)