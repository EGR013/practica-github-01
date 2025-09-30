#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
numero1=int(input("introduce un numero "))
if numero1>10:
    numero1=int(input("creo que ese numero es demasiado alto prueba con un numero que no sea mas grande que 10 "))
if numero1<0:
    numero1=int(input("creo que ese numero es demasiado bajo prueba con un numero que no sea mas pequeño que 0 "))
numero2=int(input("introduce otro numero "))
if numero2>10:
    numero2=int(input("creo que ese numero es demasiado alto prueba con un numero que no sea mas grande que 10 "))
if numero2<0:
    numero2=int(input("creo que ese numero es demasiado bajo prueba con un numero que no sea mas pequeño que 0 "))
if numero1>numero2:
    print("el numero mas grande es ",numero1,"i el mas pequeño es ",numero2)
if numero1<numero2:
     print("el numero mas grande es ",numero2,"i el mas pequeño es ",numero1)