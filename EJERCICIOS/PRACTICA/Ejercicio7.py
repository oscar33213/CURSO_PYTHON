# 7) Mayor de tres números
def ejercicio_7_mayor_de_tres(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        mayor = num1
    elif num2 >= num1 and num2 >= num3:
        mayor = num2
    else:
        mayor = num3

    return "El numero mayor es: " + str(mayor)


priemrNum = float(input("introduce el primer numero: "))
secNum = float(input("introduce el segundo numero: "))
terNum = float(input("introduce el tercer numero: "))

num1 = priemrNum
num2 = secNum
num3 = terNum

print(ejercicio_7_mayor_de_tres(num1, num2, num3))