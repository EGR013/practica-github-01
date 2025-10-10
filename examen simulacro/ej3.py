radio=int(input("porfavor introdusca el radio de este cilindro "))
altura=int(input("porfavor introdusca la altura de este cilindro "))
volumen=(radio*altura)/2 #esto esta mal
frase=("el volumen es: ",volumen)
answear=print("quiere que le digamos el resultado en mayuscula (inserte MAYUS) o en minuscula (inserte minus): ")
frase_up=(frase) #hay que poner que este en mayuscula str no funciona #porque era texto! bruuhhhh no pongas comas
frase_low=(frase) #^lo mismo pero en minus
if answear == "MAYUS":
    print(": ",frase_up)
if answear == "minus":
    print(": ",frase_low)
else:
    print("esta respuesta no conside con ninguna de las opciones porfavor intentelo de nuevo")