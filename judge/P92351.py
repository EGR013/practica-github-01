import math
t=list(str(input()).split())
a=int(t[0])
b=int(t[1])
if b<=0:
    b=float(input())
r=(math.trunc(a/b)*-b)+a
d=a//b
print(d,r)