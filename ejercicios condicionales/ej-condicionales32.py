#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas
frasemagik=("A quién madruga Dios ayuda")
word=str(input("introduce una palabra "))

if word in frasemagik:
    print("la palabra esta dento de la frase A quién madruga Dios ayuda")
if word not in frasemagik:
    print("la palabra no esta en la palabra A quién madruga Dios ayuda")