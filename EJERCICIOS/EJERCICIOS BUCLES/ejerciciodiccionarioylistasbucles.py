paises = {}



pais = input("Introduce un pais (Indica 'salir' para finalizar: ")


while pais!= "salir":
    
    ciudad = input("Añade una cudad: ")
    lista_ciudades = paises.setdefault(pais,[ciudad])
    if lista_ciudades != [ciudad]:
        paises[pais].append(ciudad)
        
    pais = input("Introduce un pais (Indica 'salir' para finalizar: ")
    
    

print(paises)



    
    