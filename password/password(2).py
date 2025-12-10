#Realiza la VERSIÓN 2 de la actividad Password utilizando bucles (for). 
#Aspectos a tener en cuenta en el desarrollo de la actividad:
#1. Realiza las modificaciones correspondientes en una copia del fichero versión 1.
#2. En esta versión, no debes contemplar que se cumplan las condiciones en las posiciones de los índices, pero sí que el total de criterios se cumplan: 3 números (distinguiendo rangos), 3 letras (distinguiendo mayúsculas o minúsculas), 2 símbolos, etc.
#3. Tiene que existir un bucle que recorra el password y realice las comprobaciones y loscontajes necesario.
#4. El usuario debe poder introducir un total de 3 passwords en una misma ejecución del programa. Además de visualizar por pantalla si el password cumple o no con los criterios, debe aparecer por pantalla el número de passwords que ha introducido con formato correcto e incorrecto.
#5. Crea un testeo de 10 pruebas que permita la evaluación del código, puedes compartir testeos con otros compañeros. Añádelos como comentario en tu código.
#6. Tienes libertad para establecer otros criterios que consideres oportunos en el programa. Explícalos con claridad a través de comentarios en el código
#7. La entrega la debes realizar por Managebac utilizando la misma publicación del Password versión 1

#saludo
print("Hola usuario!,es hora de crear una contraseña segura i fiable")
#datos iniciales
attempts=0
fails=0
correct=0
requierments=0
errores=0
simbols=0
oneup5low=0
minus=0
mayus=0
fs65=0
#esto probablemente no sera usado per bueno
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
print("  2.tener un minimo de 2 simbolos (*, _, @, &,/,#)")
print("  3.tener 2 numeros mayores o iguales que 1 i menores o iguales a 5")
print("  4.tener un minimo de 2 letras minusculas")
print("  5.un minimo de 1 letra mayuscula")
print("  6.minimo 1 número menor o igual que 6 y mayor o igual que 5")
place=0
#input de password
password=(input("muy bien hora de introducir tu password: "))
length=len(password)
#inicio de checkeo de password 
if not (len(password)>=6) and (len(password)<=8):
    print("longitud de password no valido")
else:
    for i in range(0,length):
        select=password(place)
        if select in ("*_@&/#"):
            simbols=simbols+1
        if select>=1 and select<=5:
            oneup5low=oneup5low+1
        if 
        