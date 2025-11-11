#41. Imprime el siguiente patrón utilizando for:
num=6
salida=""
for x in range(1,num):
    for i in range(1,num):
        i = (6-i)-(x-1)
        salida=salida+f"{i}"
    print(salida)
    num-=1
    salida=""