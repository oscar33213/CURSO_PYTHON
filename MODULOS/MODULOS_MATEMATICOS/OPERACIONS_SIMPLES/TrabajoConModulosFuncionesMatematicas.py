from math import sqrt

def suma():
    num1 = float(input("Indica primer valor: "))
    num2 = float(input("Indica segundo valor: "))
    
    return f"El resultado de la suma entre {num1} y {num2} es: {num1 + num2}."

def resta():
    num1 = float(input("Indica primer valor: "))
    num2 = float(input("Indica segundo valor: "))
    
    return f"El resultado de la resta entre {num1} y {num2} es: {num1 - num2}."

def multiplicacion():
    num1 = float(input("Indica primer valor: "))
    num2 = float(input("Indica segundo valor: "))
    
    return f"El resultado de la multiplicación entre {num1} y {num2} es: {num1 * num2}."

def division():
    try:
        num1 = float(input("Indica primer valor: "))
        num2 = float(input("Indica segundo valor: "))
        
        resultado = num1 / num2
        return f"El resultado de dividir {num1} entre {num2} es: {resultado}"

    except ValueError:
        return "Entrada no válida. Debes introducir números."
    except ZeroDivisionError:
        return "No se puede dividir entre 0."



