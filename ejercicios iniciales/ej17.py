#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
peso=int(input("introduce tu peso en kg "))
altura=float(input("introduce tu altura en metros "))
imc=peso/(altura**2)
print("tu peso es ",peso)
print("tu altura es ",altura)
print("por lo tanto tu imc debe de ser ",imc)
if imc>=25:
    print("hay sobrepeso")