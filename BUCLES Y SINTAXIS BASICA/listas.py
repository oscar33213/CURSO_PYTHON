#LISTAS

alumnos = ["Juan", 22, "Jorge", 21, "Pepe", 30, "Andres", 18]
#RECORRER LA LISTA
for i in alumnos:
    print(i)

#IMPRIMIR LONGITUD DE LA LISTA
print(len(alumnos))
#AÑADIR NUEVOS ELEMENTOS A LA LISTA
alumnos.append("Marcos")
alumnos.append(21)
    
    
print(alumnos)
print(len(alumnos))

#IMPRIMIR LA POSICIÓN DE UNA LISTA
print(alumnos[3])

#ACCESO A LA LISTA DESDE EL FINAL
print(alumnos[-3])

#IMPRIME EL RANGO DE LA LISTA ESPECIFICADO
print(alumnos[0:4])

