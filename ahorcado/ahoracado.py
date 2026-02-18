import random
#while true baneado
Lista_palabrasecreta=["Ahorcado","solicitar","encontrar","situación","onstruir","esperanza", "cognitivo", "condición","esbirro","Hipopotomonstrosesquipedaliofobia"]
palabrasecreta=Lista_palabrasecreta[random.randint(0,9)]
Lista_partida=[]
Lista_ahorcado=["_","_","_","_","_","_","_","_"]
errores=0
for x in range(0,len(palabrasecreta)):
    Lista_partida.append("_")


