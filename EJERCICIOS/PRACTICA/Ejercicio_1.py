# 1) Suma simple
# Pide dos números por teclado y muestra su suma.
def ejercicio_1_suma(num1, num2):
    return "La suma de: " + str(num1) + " + " +  str(num2) + " es: " + str(num1+num2)


primerNum = int(input("Introduce el primer numero: "))
secNum = int(input("Introduce el segundo numero: "))
    

num1 = primerNum
num2 = secNum


print(ejercicio_1_suma(num1, num2))