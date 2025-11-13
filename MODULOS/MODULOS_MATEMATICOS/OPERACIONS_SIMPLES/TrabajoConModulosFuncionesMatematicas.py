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
    num1 = float(input("Indica primer valor: "))
    num2 = float(input("Indica segundo valor: "))
    
    while num1 <= 0 or num2 <= 0:
        print("No se puede dividir por 0 o valores negativos")
        num1 = float(input("Indica primer valor: "))
        num2 = float(input("Indica segundo valor: "))
        
    return f"El resultado de la division entre {num1} y {num2} es: {num1 / num2}."




