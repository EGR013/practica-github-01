import random
import unicodedata
import time
import math
import datetime
#while true baneado
start=datetime.datetime.now()
start_calc=[]
start_calc.append(start.hour)
start_calc.append(start.minute)
start_calc.append(start.second)
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
choice_final=1

while choice_final==1:
    p=0
    choice_add=0
    forever=1
    lista_baneada=[]
    Lista_partida=[]
    palabrasecreta=Lista_palabrasecreta[random.randint(0,len(Lista_palabrasecreta)-1)]
    choice_add=int(input("antes de empezar quieres añadir alguna palabra a la lista de palabras secretas? si(1) o no(2): "))
    if choice_add==1:
        Lista_palabrasecreta.append(input())
        palabrasecreta=Lista_palabrasecreta[random.randint(0,len(Lista_palabrasecreta))]
    for x in range(0,len(palabrasecreta)):
        Lista_partida.append("_")
    choices_almost=1
    palabrasecreta=palabrasecreta.lower()

    while choices_almost==1:
        c=0
        print(Lista_partida)
        letra=input("ahora es hora de intentar adivinar la palabra introduce una letra: ")
        letra=letra.lower()
        if letra.isalpha() and not letra in lista_baneada:
            for i in range(0,len(palabrasecreta)):
                if letra==palabrasecreta[i]:
                    Lista_partida[i] = letra
                    c=c+1
            if c>0:
                lista_baneada.append(letra)
                lista_aciertos.append(letra)
                print("acierto",Lista_partida)
                c==0
            else:
                lista_baneada.append(letra)
                Lista_errores.append(letra)
                Lista_ahorcado_form2[p]=lista_ahorcado_form1[p]
                print("fallo",Lista_ahorcado_form2)
                c==0
                p=p+1
        if p==8:
            print("has perdido la pertida la palabra secreta era: ",palabrasecreta,"quieres iniciar otra ronda?")
            choice_final=int(input("introduce 1 si quieres continuar,introduce 0 si quieres dejar el programa: "))
            choices_almost=0
        if "_" not in Lista_partida:
            print("muy bien! la palbra correcta era",Lista_partida,"quieres jugar otra partida?")
            choice_final=int(input("introduce 1 si quieres continuar,introduce 0 si quieres dejar el programa: "))
            choices_almost=0

finish=datetime.datetime.now()
finish_calc=[]
finish_calc.append(finish.hour)
finish_calc.append(finish.minute)
finish_calc.append(finish.hour)
minuts=(finish.minute)-(start.minute)
hours=(finish.hour)-(start.hour)
seconds=(finish.second)-(start.second)
print("este es tu numero de aciertos: ",len(lista_aciertos))
print("esto es tu numero de errores: ",len(Lista_errores))
print("este es el tiempo que tardaste en acabar la partida puesto en el siguiente formato(horas:minutos:segundos) ",hours,":",minuts,":",seconds)


    


