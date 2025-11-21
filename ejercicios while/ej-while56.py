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
while repeat==1:
    selection1=int(input("seleciona el bocadillo que quieres (por numero no nombre): "))
    if selection1>3 or selection1<1:
        print("numero no presente en el menu")
        break
    if selection1==1:
        selection1=9
    if selection1==2:
        selection1=4.5
    if selection1==3:
        selection1=2.5
    selection2=int(input("seleciona el acompañamiento que deseas (por numero no por nombre): ")) 