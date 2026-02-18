ff=list(str(input()).split())
a1=ff[0]
b1=ff[1]
a2=ff[2]
b2=ff[3]
start=[]
end=[]
start.append(a1,b1)
end.append(a2,b2)

if start > end:
    print("[]")
else:
    print(f"[{start},{end}]")