import random
number=list(str(input()).split())
numa=int(number[0])
numb=int(number[1])
numc=int(number[2])
if numa>numb and numa>numc:
    print(numa)
if numb>numa and numb>numc:
    print(numb)
if numa==numb and numa==numc and numb==numc:
    print(numa)
if numc>numa and numc>numb:
    print(numc)