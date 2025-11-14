#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuariotenga x oportunidades para ver si letra introducida está en esa palabra.
palabra=str(input("introduce la palabra seceta: "))
intentos=len(palabra)
for i in range(0,intentos):
    word=str(input("introduce una letra: "))
    if word in palabra:
        print("esta letra esta en la palabra secreta")
    else:
        print("esta letra no esta en la palabra secreta")
print("te has quedado sin intentos")