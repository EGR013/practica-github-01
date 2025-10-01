#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
nota=int(input("dime tu nota "))
if nota <= 5:
    print("felicidades estas aprovado!")
if nota > 5:
    print("losiento estas suspendido")
    if nota > 10:
        print("creo que esta nota es demasiado alta intentalo otra vez con una nota que no sea mas grande que 10")
if nota < 0:
        print("creo que esa nota es demasiado baja intentalo otra vez con una nota que no sea mas pequeño que 0")