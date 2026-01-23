#85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el programa debe mostrar la media y mediana los todos los alumnos introducidos
ingles=[]
castellano=[]
catalan=[]
helpme=120
subject=0
while helpme==120:
    select=input("introdeuce el nombre de el alumno: ")
    ing=float(input("introduce su nota de ingles: "))
    ingles.append(ing) 
    select=input("introdeuce el nombre de el alumno: ")
    cas=float(input("introduce su nota de castellano: "))
    castellano.append(cas)
    select=input("introdeuce el nombre de el alumno: ")
    cat=float(input("introduce su nota de catalan: "))
    catalan.append(cat)
    subject=subject+1
    choice=int(input("quieres continuar si(1) no(2)"))
    if choice==1:
        break

print("RESUMEN")
print("la media de ingles es: ",sum(ingles)/subject)
print("la media de castellano es: ",sum(castellano)/subject)
print("la media de catalan es: ",sum(catalan)/subject)

longitud=len(castellano)
longitud=len(catalan)
length=len(ingles)

print("la mediana de ingles es: ",ingles[length/2])
print("la mediana de castellano es: ",castellano[longitud/2])
print("la mediana de catalan es: ",catalan[longitud/2])