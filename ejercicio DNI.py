listaalpha= 'TRWAGMYFPDXBNJZSQVHLCKE'
#dni=input("introduce los numeros de tu DNI son 8 digitos: ")
lista_intentos=[]
good=0
choice=1
choices=0
dnis=[]
correct=[]
incorrect=[]
while choice==1:
    dni=input("introduce los numeros de tu DNI son 8 digitos: ")
    if len(dni)==8:
        if dni.isnumeric():
            resto=int(dni)%23
            letra=listaalpha[resto]
            if resto < 23 and resto >= 0:
                lista_intentos.append(3)
                nif = f"{dni}-{letra}"
                print(nif)
                dnis.append(dni)
                correct.append(nif)
                choice=input("Quieres continuar? si(1) o no(2): ")
                
            else:
                print("error")
                lista_intentos.append(2)
                dnis.append(dni)
                incorrect.append(dni)
                choice=input("Quieres continuar? si(1) o no(2): ")
        else:
            print("error")
            lista_intentos.append(1)
            dnis.append(dni)
            incorrect.append(dni)
            choice=input("Quieres continuar? si(1) o no(2): ")
    else:
        print("error")
        lista_intentos.append(0)
        dnis.append(dni)
        incorrect.append(dni)
        choice=input("Quieres continuar? si(1) o no(2): ")

correct.sort()
incorrect.sort()
lengthtotal=len(lista_intentos)
cero=lista_intentos.count(0)
uno=lista_intentos.count(1)
dos=lista_intentos.count(2)
totalerrores=cero+uno+dos
totalcorrectos=lista_intentos.count(3)
porcentajeokay=int(lengthtotal%totalcorrectos)
porcentajenookay=int(lengthtotal%totalerrores)
porcentajecero=int(lengthtotal%cero)
porcentajeuno=int(lengthtotal%uno)
porcentajedos=int(lengthtotal%dos)
while choices==0:
    choice2=int(input("escoje la opcion que te interesa: 1.listar NIF correctos ordenados de menor a mayor 2.Listar DNI incorrectos ordenados de menor a mayor 3.Número total de errores 4.Número total de DNIs correctos. 5.porcentaje de DNI correctos, incorrectos, errores de longitud, errores de número, no existentes. 6.abandonar el programa: "))
    if choice2==1:
        print("Lista de NIFs correctos ordenados de menor a mayor: ",correct)
        choices=1
    if choice2==2:
        print("Lista de DNIs incorrectos ordenados de menor a mayor: ",incorrect)
        choices=2
    if choice2==3:
        print("Número total de errores: ",totalerrores)
        choices=3
    if choice2==4:
        print("Número total de DNIs correctos: ",totalcorrectos)
        choices=4
    if choice2==5:
        print("porcentaje de dnis correctos: ",porcentajeokay)
        print("porcentaje de dnis incorrectos: ",porcentajenookay)
        print("porcentaje de errores de lonjitud: ",porcentajecero)
        print("porcentaje errores de numero: ",porcentajeuno)
        print("porcentaje errores de dni no existentes: ",porcentajedos)
        choices=5
    if choice2==6:
        print("FIN DEL PROGRAMA")
        choices=6
    else:
        print("ERROR intentalo otra vez")

#list(dni).append("-",letra)
#print("dni")
