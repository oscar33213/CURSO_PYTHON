# 5) Temperatura
# Convierte grados Celsius a Fahrenheit.
def ejercicio_5_celsius_a_fahrenheit(grados):
    
    return "La temperatura de: " + str(grados) + " ºC a Fahrenheit es: " + str((grados*1.8)+ 32) + " ºF"


gradosC = float(input("Introduce los grados en Celsius "))

grados = gradosC

print(ejercicio_5_celsius_a_fahrenheit(grados))