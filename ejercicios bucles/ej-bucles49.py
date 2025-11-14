#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.

palabra=str(input("introduce la palabra seceta: "))
intentos=len(palabra)
for i in range(intentos):
    word=str(input("introduce una letra: "))
    if word in palabra:
        for j in range(intentos):
            if word is palabra[j]:
                print(f"La {word} está en la posición {j + 1}. ")
    else:
        print("esta letra no esta en la palabra secreta")
print("te has quedado sin intentos")