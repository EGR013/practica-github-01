year=input()
if year[2] and year[3]==0:
    list.pop(0)
    if list%4==0:
        print("YES")
    else:
        print("NO")
else:
    if year%4==0:
        print("YES")
    else:
        print("NO")
