nombre=str(input("introduce tu nombre: "))
edad=int(input("introduce tu edad: "))
año_actual=2025
if edad>0 and edad<100:
    futuro=año_actual - edad + 100
    print(" hola: ",nombre,"cumpliras 100 años en el año: ",futuro)
else:
    print("tu edad no es valida")