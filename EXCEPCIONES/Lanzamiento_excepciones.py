import math


def CalculaRaizC(numero):
    
    if numero < 0:
        raise ValueError ("El numero no puede ser negativo") #LANZAMIENTO DE EXCEPCIONES
    else:
        return math.sqrt(numero)

numeroUsuario = float(input("Indica un un numero: "))
try:
    print(CalculaRaizC(numeroUsuario))
except ValueError:
    print("ERROR NUMERO NEGATIVO")
    
print("Sigue el programa...")