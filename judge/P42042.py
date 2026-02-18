letra=input()
import random
life=1
death=2
limbo=0
isodamion=1
permanent=0
letra1=letra
for x in range(1,1000):
    limbo=random.randint(life,death)
    if limbo==life:
        letra=letra.upper()
    if limbo==death:
        letra=letra.lower()
    
    if letra1==letra:
        if limbo==life:
            print("uppercase")
        if limbo==death:
            print("lowercase")
        break
    else:
        limbo=0
        isodamion=isodamion+1



if letra in ("aiuoeAEIOU"):
    print("vowel")
else:
    print("consonant")