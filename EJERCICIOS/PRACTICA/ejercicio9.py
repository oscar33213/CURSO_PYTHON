

# 9) Clasificación por notas
# Nota de 0 a 10 -> "Suspenso", "Aprobado", "Notable", "Sobresaliente"
def ejercicio_9_clasificacion_notas():
    nota = float(input("Introduce una nota: "))

    while nota < 0 or nota > 10:
        print("❌ Solo valores entre 0 y 10.")
        nota = float(input("Introduce una nota válida: "))

    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Notable"
    elif nota >= 5:
        return "Aprobado"
    else:
        return "Suspenso"


resultado = ejercicio_9_clasificacion_notas()
print("Resultado:", resultado)
