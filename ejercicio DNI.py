listanumeric=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22"]
listaalpha=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
#dni=input("introduce los numeros de tu DNI son 8 digitos: ")
lista_intentos=[]
good=0
choice=1
dnis=[]
correct=[]
incorrect=[]
while choice==1:
    dni=input("introduce los numeros de tu DNI son 8 digitos: ")
    if len(dni)==8:
        if dni.isnumeric:
            resto=dni%23
            letra=listaalpha[resto]
            if resto not in listanumeric:
                print("error")
                lista_intentos.append(2)
                dnis.append(dni)
                incorrect.append(dni)
                choice=input("Quieres continuar? si(1) o no(2): ")
            else:
                lista_intentos.append(3)
                list(dni).append("-",letra)
                print("dni")
                dnis.append(dni)
                correct.append(dni)
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

choice2=input("escoje la opcion que te interesa: 1.listar DNI correctos ordenados de menor a mayor 2.Listar DNI incorrectos ordenados de menor a mayor 3.Número total de errores 4.Número total de DNIs correctos. 5.porcentaje de DNI correctos, incorrectos, errores de longitud, errores de número, no existentes.")
correct.sort()
incorrect.sort()
lengthtotal=len(lista_intentos)
cero=lista_intentos.count(0)
uno=lista_intentos.count(1)
dos=lista_intentos.count(2)
totalerrores=cero+uno+dos
totalcorrectos=lista_intentos.count(3)
porcentajeokay=lengthtotal%totalcorrectos
porcentajenookay=lengthtotal%totalerrores
porcentajecero=lengthtotal%cero
porcentajeuno=lengthtotal%uno
porcentajedos=lengthtotal%dos
print("Lista de DNIs correctos ordenados de menor a mayor: ",correct)
print("Lista de DNIs incorrectos ordenados de menor a mayor: ",incorrect)
print("Número total de errores: ",totalerrores)
print("Número total de DNIs correctos: ",totalcorrectos)
print("porcentaje de dnis correctos: ",porcentajeokay)
print("porcentaje de dnis incorrectos: ",porcentajenookay)
print("porcentaje de errores de lonjitud: ",porcentajecero)
print("porcentaje errores de numero: ",porcentajeuno)
print("porcentaje errores de dni no existentes: ",porcentajedos)
#list(dni).append("-",letra)
#print("dni")
