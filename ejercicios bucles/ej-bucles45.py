#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el stringdistinguiendo vocales y las consonantes:
palabra=str(input("introduse una palabra: "))
num=0
palabra=palabra.lower()
vocales=""
consonantes=""
pal_count=len(palabra)
for i in range(0,pal_count):
    if palabra[num] in ("a,i,e,u,o,á,é,í,ó,ú,ü,"):
        vocales=vocales+palabra[num]
        num=num+1
    else:
        consonantes=consonantes+palabra[num]
        num=num+1
print("las vocales de esta palabra son: ",vocales,"i las consonantes son: ",consonantes)
    