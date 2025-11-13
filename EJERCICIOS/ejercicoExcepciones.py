ListaNombres = []

while (len(ListaNombres)) < 11:
    nombre = input("Introduce un nombre: ")
    try:
        if nombre in ListaNombres:
            raise ValueError("Este nombre ya existe.")
        ListaNombres.append(nombre)
    except ValueError as e:
        print(e, nombre)

for i in ListaNombres:
    print(i)
