
number=list(str(input()).split())
if len(number)==2:
    b=input()
    number.append(input())
    if len(number)<3:
        number.append(input())

numbers=int(number[0])+int(number[1])+int(number[2])
print(numbers)