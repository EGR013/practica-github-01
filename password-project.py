print("Hola usuario!,es hora de crear una contraseña segura i fiable")
errores=0
posicion1="posicion 1"
posicion2="posicion 2"
posicion3="posicion 3"
posicion4="Posicion 4"
posicion5="posicion 5"
posicion6="posicion 6"
posicion7="posicion 7"
posicion8="posicion 8"
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
password=(input("muy bien ya sabes las normas hora de introducir tu password!: "))
if len(password) >= 6 and len(password)<=8:
    print("esta contraseña no tiene una longitud apropiada intentalo de nuevo")
    if password[0] >5 and password[0]<1:
        print("a") , posicion1=""
    else:
        errores=errores + 1
    if password[1].isalpha() and password[1].islower():
       print("a") , posicion2=""
    else:
        errores=errores + 1
    if password[2].isalpha() and password[2].isupper():
        print("a") , posicion3=""
    else:
        errores=errores+1
    if password[3] in ("*_@"):
        print("a") , posicion4=""
    else:
        errores=errores+1
    if password[4].isalpha() and password[4].islower():
        print("a") , posicion5=""
    else:
        errores=errores+1
    if password[5]>= 6  and password[5]<=9:
        print("a") , posicion6=""
    else:
        errores=errores+1
    if password[6] in ("&/#"):
        print("a") , posicion7=""
    else:
        errores=errores+1
    if password[7]<=5:
        print("a") , posicion8=""
    else:
        errores=errores+1
else:
    print("esta contraseña no es apropiada intentalo de nuevo")
    

