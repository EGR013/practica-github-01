#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida
a=int(input("introduce el pimer intervalo: "))
b=int(input("introduce el segundo intervalo: "))
if a<b:
    for i in range(a,b):
        if a<b:
            print(a,end="-")
            a=a+1
    print(a)
if a>b:
    for i in range(b,a):
        if a>b:
            print(a,end="-")
            a=a-1
    print(a)