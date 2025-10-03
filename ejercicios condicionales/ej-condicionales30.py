#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif
frase=str(input("porfavor introdece una frase "))
longitud = len(frase)
if longitud==11:
    print("esta frase tiene caracteres iguales a 11")
    
if longitud >11:
 print("esta frase tiene caracteres mayores que 11")
 
if longitud <11:
    print("esta frase tiene caracteres menores que 11")