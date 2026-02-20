import random
import unicodedata
import time
import math
#while true baneado
Lista_palabrasecreta=["Ahorcado","solicitar","encontrar","situación","onstruir","esperanza", "cognitivo", "condición","esbirro","Hipopotomonstrosesquipedaliofobia"]
Lista_partida=[]
lista_ahorcado_form1=["A","H","O","R","C","A","D","O"]
Lista_ahorcado_form2=["_","_","_","_","_","_","_","_"]
Lista_errores=[]
lista_aciertos=[]
lista_baneada=[]
life=[]
death=[]
letra=""
while choice_final==1:
    choice_add=0
    choice_final=0
    forever=1
    lista_baneada=[]
    palabrasecreta=Lista_palabrasecreta[random.randint(0,len(palabrasecreta))]
    choice_add=input(int("antes de empezar quieres añadir alguna palabra a la lista de palabras secretas? si(1) o no(2): "))
    if choice_add==1:
        Lista_palabrasecreta.append(input())
        Lista_palabrasecreta=Lista_palabrasecreta[random.randint(0,len(Lista_palabrasecreta))]
    for x in range(0,len(palabrasecreta)):
        Lista_partida.append("_")

    while choice_final==0:
        c=0
        print(Lista_partida)
        letra=input("ahora es hora de intentar adivinar la palabra introduce una letra: ")
        if letra.isalpha and not in lista_baneada:
            for i in range(0,len(palabrasecreta)):
                if letra==palabrasecreta[i]:
                    palabrasecreta[i] = letra
                    c=c+1
            if c>0:

            #if c==0:
                



    


