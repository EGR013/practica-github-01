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
lonjitud=len(catalan)
length=len(ingles)
if length%2==0:
    mi=ingles[length/2]/ingles[(length/2)-1]
else:
    mi=ingles[length/2]
if longitud%2==0:
    mcas=castellano[longitud/2]/castellano[(longitud/2)-1]
else:
    mcas=castellano[longitud/2]
if lonjitud%2==0:
    mcat=catalan[lonjitud/2]/catalan[(lonjitud/2)-1]
else:
    mcat=catalan[lonjitud/2]

print("la mediana de ingles es: ",mi)
print("la mediana de castellano es: ",mcas)
print("la mediana de catalan es: ",mcat)