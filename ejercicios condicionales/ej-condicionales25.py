#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
nota=float(input("dime tu nota "))
nota=round(nota,1)
if nota >=8.5 and nota<=10:
     print("tu nota es: ",nota,"felicidades es un excelente!!")
if nota >=6.5 and nota<8.5 :
    print("tu nota es: ",nota,"felicidades es un notable")
if nota<6.5 and nota>=5:
     print("tu nota es: ",nota,"es un suficiente")
if nota < 5:
    print("tu nota es: ",nota,"losiento estas suspendido")
    if nota > 10:
        print("creo que esta nota es demasiado alta intentalo otra vez con una nota que no sea mas grande que 10")
if nota < 0:
        print("creo que esa nota es demasiado baja intentalo otra vez con una nota que no sea mas pequeño que 0")