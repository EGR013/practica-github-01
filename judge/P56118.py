import random
number=list(str(input()).split())
numa=number[0]
numb=number[1]
if float(numa)>float(numb):
    if float(numa)>0:
        print(numa)
    else:
        print(numb)
if float(numa)<float(numb):
    if float(numb)>0:
        print(numb)
    else:
        print(numa)
if float(numa)==float(numb):
    print(numa)