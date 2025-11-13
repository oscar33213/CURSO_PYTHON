from math import *


def Potencia():
    base = float(input("Indica la base: "))
    expo = int(input("Indica el exponente: "))
    
    return f"El numero {base} elevado a {expo} es: {round(base**expo)}"


def raizC():
    num1 = float(input("Indica primer valor: "))
    while (num1 < 0):
        print ("No se puede calcular la raiz de un valor negativo")
        num1 = float(input("Indica primer valor: "))
    return f"El resulatdo d ela raiz cuadrada de {num1} es: {sqrt(num1)}"
    
def Redondeo():
    num = float(input("Indica el numero a redondear: "))
    
    return f"El redonde de {num} es: {round(num)}"

