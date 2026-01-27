listanumeric=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22"]
listaalpha=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
#dni=input("introduce los numeros de tu DNI son 8 digitos: ")
lista_intentos=[]
good=0
choice=1
while choice==1:
    dni=input("introduce los numeros de tu DNI son 8 digitos: ")
    if len(dni)==8:
        if dni.isnumeric:
            resto=dni%23
            letra=listaalpha[resto]
            if resto not in listanumeric:
                print("error")
                lista_intentos.append(2)
            else:
                lista_intentos.append(3)
                list(dni).append("-",letra)
                print("dni")
        else:
            print("error")
            lista_intentos.append(1)
    else:
        print("error")
        lista_intentos.append(0)

#list(dni).append("-",letra)
#print("dni")
