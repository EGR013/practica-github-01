#saludo
print("Hola usuario!,es hora de crear una contraseña segura i fiable")
#datos iniciales
errores=0
posicion1="posicion 1"
posicion2="posicion 2"
posicion3="posicion 3"
posicion4="Posicion 4"
posicion5="posicion 5"
posicion6="posicion 6"
posicion7="posicion 7"
posicion8="posicion 8"
#instruciones
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
#input de password
password=(input("muy bien ya sabes las normas hora de introducir tu password!: "))
#checkeo de password
if (len(password)>=6) and (len(password)<=8):
    p0=float(password[0])
    p1=password[1]
    p2=password[2]
    p3=password[3]
    p4=password[4]
    p5=float(password[5])
    p6=password[6]
    p7=float(password[7])
    if p0<=5 and p0>=1:
        posicion1=("")
    else:
        errores=errores + 1
    if p1.isalpha() and p1.islower():
       posicion2=("")
    else:
        errores=errores + 1
    if p2.isalpha() and p2.isupper():
        posicion3=("")
    else:
        errores=errores + 1
    if p3 in ("*_@"):
        posicion4=("")
    else:
        errores=errores + 1
    if p4.isalpha() and p4.islower():
        posicion5=("")
    else:
        errores=errores + 1
    if p5>= 6  and p5<=9:
        posicion6=("")
    else:
        errores=errores + 1
    if p6 in ("&/#"):
        posicion7=("")
    else:
        errores=errores + 1
    if p7<=5:
        posicion8=("")
    else:
        errores=errores + 1 
        #resultados finales
    if errores==0:
     print("este password es correcto , felicidades! esperamos que esto te ayude a tener mas seguridad digital")
    else:
     print("este password tiene un total de: ",errores,"errores estos esrrores estan en las siguientes posiciones: ",posicion1,"",posicion2,"",posicion3,"",posicion4,"",posicion5,"",posicion6,"",posicion7,"",posicion8)
else:  
    print("la longitud de esta contraseña no es apropiada ya que su longitud es de",len(password),"intentalo de nuevo") 