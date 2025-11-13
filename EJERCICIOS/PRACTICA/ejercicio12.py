def ejercicio_12_suma_hasta_cero():
    numeros_a_sumar = []
    
    while True:
        numero = int(input("Introduce un número (0 para terminar): "))
        if numero == 0:
            break
        numeros_a_sumar.append(numero)
    
    return sum(numeros_a_sumar)


# Programa principal
print("Suma total:", ejercicio_12_suma_hasta_cero())

