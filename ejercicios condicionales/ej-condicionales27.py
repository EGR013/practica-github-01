#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla
letra=str(input("introduce una letra "))
if len(letra) != 1 or not letra.isalpha():
        print("esto no es una letra porfavor vuelvelo a intentar")
if letra.isupper():
        print("la letra es mayuscula")
if letra.islower():
        print("la letra es minuscula")