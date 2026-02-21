n=int(input())
h=n//3600
remaining=n%3600
m=remaining//60
s=remaining %60
print(h,m,s)
