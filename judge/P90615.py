import random
number=list(str(input()).split())
numa=int(number[0])
numb=int(number[1])
numc=int(number[2])
ans=0
while ans==0:
    if numa>numb and numa>numc:
        print(numa)
        break
    if numb>numa and numb>numc:
        print(numb)
        break
    if numa==numb and numa==numc and numb==numc:
        print(numa)
        break
    if numc>numa and numc>numb:
        print(numc)
        break
    if numa==numc and numa>numb:
        print(numa)
        break
    if numa==numb and numa>numc:
        print(numa)
        break
    if numb==numc and numb>numa:
        print(numb)
        break
    if numb==numa and numb>numc:
        print(numb)
        break
    if numc==numb and numc>numa:
        print(numc)
        break
    if numc==numa and numc>numb:
        print(numc)
        break