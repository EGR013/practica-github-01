#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.
frasemagik=("A quién madruga Dios ayuda")
word=str(input("introduce una palabra "))

if word in frasemagik:
    print("la palabra esta dento de la frase A quién madruga Dios ayuda")
if word not in frasemagik:
    print("la palabra no esta en la palabra A quién madruga Dios ayuda")