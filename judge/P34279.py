n=input().split()
h=int(n[0])
m=int(n[1])
s=int(n[2])
s=s+1
if s==60:
    s=0
    m+=1
if m==60:
    m=0
    h+=1
if h==24:
    h=0

print(f"{h:02}:{m:02}:{s:02}")
