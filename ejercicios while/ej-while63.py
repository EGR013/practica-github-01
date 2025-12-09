#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el númerode veces que se repite cada número.
import random
one=0
two=0
tres=0
four=0
five=0
six=0
for i in range(0,100):
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
print("uno: ",one)
print("dos: ",two)
print("tres: ",tres)
print("cuatro: ",four)
print("cinco: ",five)
print("seis: ",six)