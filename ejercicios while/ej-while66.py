#66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo se comporta el dado en lanzamientos producidos durante aprox 3 segundos
import time
import random
inicio=time.time()
one=0
two=0
tres=0
four=0
five=0
six=0
while (time.time()-inicio) < 3:
    num=random.randint(1,6)
    if num==1:
        one=one+1
    if num==2:
        two=two+1
    if num==3:
        tres=tres+1
    if num==4:
        four=four+1
    if num==5:
        five=five+1
    if num==6:
        six=six+1
timeresult=time.time()-inicio
print("uno: ",one)
print("dos: ",two)
print("tres: ",tres)
print("cuatro: ",four)
print("cinco: ",five)
print("seis: ",six)
print("tiempo: ",timeresult)
