#open()
#r: Abrir fichero para lectura. El puntero se posiciona al principio del fichero
#r+: Abrir fichero para lectura y escritura. El puntero se posiciona al principio del fichero
#w: Trunca a cero la longitud o crea un fichero de texto para escritura. El puntero se posiciona al principio del fichero
#w+: Abrir fichero para lectura y escritura. Si el fichero no existe, se crea, de lo contrario se trunca. El puntero se posiciona al principio del fichero
#a: Abrir fichero para lectura. Se creará el fichero si no exsite. El puntero se posiciona al final del fichero.
#a+: Abrir fichero para lectura y escritura. Se creará el fichero si no exsite. El puntero se posiciona al final del fichero.

total = open("Text.txt","r")
texto = total.read()
print(texto)