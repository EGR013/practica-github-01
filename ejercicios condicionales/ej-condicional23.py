#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógico
nota=int(input("dime tu nota "))
if nota >=8.5 and nota<=10:
     print("felicidades es un excelente!!")
if nota >=6.5 and nota<8.5 :
    print("felicidades es un notable")
if nota<6.5 and nota>=5:
     print("es un suficiente")
if nota < 5:
    print("losiento estas suspendido")
    if nota > 10:
        print("creo que esta nota es demasiado alta intentalo otra vez con una nota que no sea mas grande que 10")
if nota < 0:
        print("creo que esa nota es demasiado baja intentalo otra vez con una nota que no sea mas pequeño que 0")