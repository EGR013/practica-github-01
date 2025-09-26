#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
adultos=int(input("introduce la cantidad de adultos "))
menores=int(input("introduce la cantidad de menores de 18 "))

adultostotal=10.8*adultos
childtotal=6*menores

print("El precio total del cine para el/los menor/es es",adultostotal)
print("El precio total del cine para el/los adulto/s es ",childtotal)