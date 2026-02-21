import math
fahhh=0.5
helpme=5
x = float(input())
if x>150000:
    while fahhh>x==False:
        if fahhh==x:
            x=x+0.01
            fahhh=fahhh+1
        if fahhh>1000:
            break
        else:
            fahhh=fahhh+1

floor_x = math.floor(x)
ceil_x = math.ceil(x)
round_x = math.floor(x + 0.5)
print(floor_x, ceil_x, round_x)

#fuente:https://www.w3schools.com/python/python_math.asp
