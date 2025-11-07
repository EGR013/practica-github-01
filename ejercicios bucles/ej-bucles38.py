#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10
numb=int(input("introduce el numero de notas que quieres introducir: "))
for i in range(1,numb+1):
    nota=float=("introduce una nota: ")
    if 0>nota or 10<nota:
        print("esta nota no es correcta")
    if nota>5 or nota==5:
        print("felicidades! estas aprovado")
    else:
        print("siento mucho informarte de que estas suspendido")