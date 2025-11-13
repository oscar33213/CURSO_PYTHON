#TUPLAS

trabajadores = ("Marta",
                "Jorge",
                "Juan",
                "Mateo")
#FUNCION QUE CONVIERTEUNA TUPLA EN LISTA
listaTrabajadores=list(trabajadores)


#IMPRIMIR TUPLAS
print(trabajadores)
#COMPROBACIÓN DE QUE SE A CONVERTIDO EN UNA LISTA
listaTrabajadores.append("Chema")
print(listaTrabajadores)

#FUNCION QUE CONVIERTE UNA LISTA EN TUPLA
tuplaTrabajadores = tuple(listaTrabajadores)

print(tuplaTrabajadores)

#FUNCION PARA SABER SI UN ELEMENTO ESTA EN LA TUPLA

print("Marta" in tuplaTrabajadores)
print(21 in tuplaTrabajadores)


#CONOCER LAS VECES QUE SEENCUENTRA UN ELEMENTO

print(tuplaTrabajadores.count("Jorge"))

print("Marta se encuentra un total de " + str(tuplaTrabajadores.count("Marta")) + " veces")


#CONOCR EL NUMERO DE ELEMENTOS

print(len(tuplaTrabajadores))

print("El numero de elementos en la tupla es de: " + str(len(tuplaTrabajadores)) + " elementos")

#DESEMPAQUETADO DE TUPLA

gerente, trabajador, coordinador, empleado1, empleado2 = tuplaTrabajadores

#CADA VARIABLE SE ASOCIA A LA POSICION EN LA TUPLA. (gerente:Marta) DEBIDO A QUE Marta SE ENCUENTRA EN LA POSICIÓN 0 

print(trabajador)


