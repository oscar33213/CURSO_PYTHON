from math import *


def Potencia():
    try:
        base = float(input("Indica la base: "))
        expo = int(input("Indica el exponente: "))
        resultado = base ** expo
        return f"El número {base} elevado a {expo} es: {resultado}"
    except ValueError:
        return "Entrada no válida"
    except OverflowError:
        return "Número demasiado grande"
    except ZeroDivisionError:
        return "No se puede elevar 0 a un exponente negativo"


import math

def raizC():
    while True:
        try:
            num1 = float(input("Indica el valor: "))
            if num1 < 0:
                print("No se puede calcular la raíz de un número negativo. Intenta de nuevo.")
                continue
            resultado = math.sqrt(num1)
            return f"El resultado de la raíz cuadrada de {num1} es: {resultado}"
        except ValueError:
            print("Entrada no válida. Debes introducir un número.")

    
def Redondeo():
    try:
        num = float(input("Indica el número a redondear: "))
        return f"El redondeo de {num} es: {round(num)}"
    except ValueError:
        return "Entrada no válida. Debes introducir un número."


