# 4) Operaciones con cadenas
# Pide un nombre y muestra cuántas letras tiene.
def ejercicio_4_longitud_nombre(nombre):
    return "El nombre: " + nombre + " tiene: " + str(len(nombre)) + " caracteres"



nombreintroducir = input(" Introduce un nombre: ")

nombre = nombreintroducir

print(ejercicio_4_longitud_nombre(nombre))