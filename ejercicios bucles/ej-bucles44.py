#44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’
numero=0
resultado=(",")
coma=(",")
for i in range(0,34):
    if numero<99:
        print(numero, end=",")
        numero=numero+3
print(numero)
