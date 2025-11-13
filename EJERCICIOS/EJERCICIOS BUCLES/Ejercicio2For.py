# Programa que muestra los números primos entre dos números introducidos por consola

# Pedimos los dos números
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Nos aseguramos de que num1 sea el menor y num2 el mayor
if num1 > num2:
    num1, num2 = num2, num1

print(f"\nNúmeros primos comprendidos entre {num1} y {num2}:\n")

# Función para comprobar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Recorremos el rango y mostramos los primos
for numero in range(num1, num2 + 1):
    if es_primo(numero):
        print(numero)

