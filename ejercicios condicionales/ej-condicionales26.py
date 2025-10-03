#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición
letra=str(input("introduce una letra "))
if letra.isupper():
        print("la letra es mayuscula")
if letra.islower():
        print("la letra es minuscula")