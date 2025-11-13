# 8) Año bisiesto
def ejercicio_8_es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return "El año: " + str(año) + " es bisiesto"
    else:
        return "El año: " + str(año) + " no es bisiesto"


añoB = int(input("Introduce el año: "))

año = añoB

print(ejercicio_8_es_bisiesto(año))