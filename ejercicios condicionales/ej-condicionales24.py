#24. Corrige los errores del siguiente código y comprueba que se ejecuta correctamente
var01=float(input("Introduce el peso: "))
var02=float(input("Introduce la altura: "))
var_imc=var01 / (var02**2)
print("si tu peso es ",var01)
print("si tu altura es ",var02)
print("entonces tu imc debe de ser ",var_imc)
if var_imc>=25:
 print("Hay sobrepeso")
else:
 print("Estás dentro de los parámetros normales")