n=int(input())
h=n//24
restante=n%3600
m=restante//60
s=restante%60
print(h,":",m,":",s)
