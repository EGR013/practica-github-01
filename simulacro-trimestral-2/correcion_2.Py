contraseña="abc123-Password1-1234-Admin2024-test"
tipo1="segura"
tipo2="devil"
tipo3="invalida"
lista=list(input())

for x in lista:
    numletras=0
    numnumeros=0
    numerocaracteres=0
    for j in x:
        if j.isnumeric():
            numnumeros+=1
        elif j.isalpha():
            numletras+=1
        else:
            numerocaracteres+=1

    if numerocaracteres==0 and len(x)>=8 and numnumeros>1 and numletras>1:
        print("la contraseña ",x,"es segura")
    if numerocaracteres==0 and len(x)<8 and (numnumeros>1 or numletras>1):
        print("la contaseña ",x,"es debil")
    if numerocaracteres>=1:
        print("la contraseña ",x,"es invalida")