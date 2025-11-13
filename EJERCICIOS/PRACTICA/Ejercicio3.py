# 3) Área de un triángulo
# Pide base y altura y muestra el área.
def ejercicio_3_area_triangulo(base, altura):
    return "El area del triangulo es de: " + str(base*altura/2)


baseTriangulo = float(input("Indica la base del Triangulo: "))
alturaTriangulo = float(input("Indica la altura del traiangulo: "))

base = baseTriangulo
altura = alturaTriangulo

print(ejercicio_3_area_triangulo(base, altura))
