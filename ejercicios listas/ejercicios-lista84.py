#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra.

import random
desorden=[]
sup=1
wha=420
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
digito=random.choice(lista)
max=len(digito)
for i in range(0,max):
    desorden.append(digito[i])
random.shuffle(desorden)
print(desorden)
while sup==1:
    print(lista)
    orden=input("identifica que palabra de la lista eran originalmente esta letras: ")
    if orden==digito:
        print("muy bien eso es correcto")
        sup=wha+sup
    else:
        print("intentalo otra vez")