#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro
print("imagina un trapecio isósceles")
lado=int(input("introduce el lado "))
basemenor=int(input("introduce la base menor "))
basemayor=int(input("introduce la base mayor "))
altura=int(input("introduce la altura "))
perimetro=basemayor+basemenor+(2*lado)
area=((basemayor+basemenor)*altura)/2
print("el perimetro es ",perimetro)
print("la area es ",area)