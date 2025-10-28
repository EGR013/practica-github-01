print("Hola usuario!,es hora de crear una contraseña segura i fiable")
errores=0
print("INSTRUCIONES")
print("  1.la longitud de el password tiene que ser entre 6 i 8 caracteres")
print("  2.forçar los siguientes valores segun la possicion indicada:")
print("     posicion 1: un numero mayor o igual a 1 i menor o igual a 5")
print("     posicion 2: una letra minuscula")
print("     posicion 3: una letra mayuscula")
print("     posicion 4: un dels seguents simbols *, _,@")
print("     Posicion 5: una lletra minuscula")
print("     posicion 6: un numero major o igual a 6 i menor o igual a 9")
print("     posicion 7: un dels seguents simbols: &,/,#")
print("     posicion 8: un numero menor o igual que 5")
password=int(input("muy bien ya sabes las normas hora de introducir tu password!: "))
if len(password) >= 6 or len(password)<=8:
    print("esta contraseña no tiene una longitud apropiada intentalo de nuevo")
    if password[0] >5 or password<1:

    
    if password[1].isalpha():
else:
    print("esta contraseña no es apropiada intentalo de nuevo")

