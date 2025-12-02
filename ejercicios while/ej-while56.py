#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la realización de un pedido, si quiere gestionar otro. El establecimiento contempla los siguientes descuentos:Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:• El número de pedidos realizados• Total a pagar.• Total con IVA (10%)• Total con el descuento aplicado.
print("MENÚ")
print("1. Bocadillo de calamares- 9 €")
print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €")
print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €")
print("3. Patatas rústicas - 2 €")
print("BEBIDAS")
print("1. Coca cola - 2 €")
print("2. Acuarius - 1.5 €")
print("3. Agua - 1 €")
repeat=1
pedidos=0
suma=0
while repeat==1:
    pedidos=pedidos+1
    selection1=float(input("seleciona el bocadillo que quieres (por numero no nombre): "))
    if selection1>3 or selection1<1:
        print("numero no presente en el menu")
        break
    if selection1==1:
        selection1=9
    if selection1==2:
        selection1=4.5
    if selection1==3:
        selection1=2.5
    selection2=float(input("seleciona el acompañamiento que deseas (por numero no por nombre): ")) 
    if selection2>3 or selection2<1:
        print("numero no presente en el menu")
        break
    if selection2==1:
        selection2=1.5
    if selection2==2:
        selection2=1.75
    if selection2==3:
        selection2=2
    selection3=float(input("seleciona la bebida que deseas (por numero no nombre)"))
    if selection3>3 or selection3<1:
        print("numero no presente en el menu")
        break
    if selection3==1:
        selection3=2
    if selection3==2:
        selection3=1.5
    if selection3==3:
        selection3==1
    suma=suma+selection1+selection2+selection3
    choice=int(input("quieres continuar 1.si , 2.no (introducelo por numero): "))
    if choice==2:
        iva=suma+(suma%10)
        if suma>19 or suma<31:
            descuento=suma-(5%suma)
            porcentaje=5
        else:
            descuento=suma-(15%suma)
            porcentaje=15
        print("pedidos totales: ",pedidos)
        print("total a pagar: ",suma)
        print("total con iva: ",iva)
        print("total con descuento de ",porcentaje,"%: ",descuento)
        break

        

