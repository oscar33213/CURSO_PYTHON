#DICCIONARIOS



salarioPersonal = {"Marcos": 1200,
                  "Jorge": 1100,
                  "Mateo": 1450,
                  "Jose Maria": 1050}

print(salarioPersonal)


#AÑADIR UN ELEMENTO AL DICCIONARIO

salarioPersonal["Manolo"]= 950   # -> nombreDiccionario[clave] = valor

print(salarioPersonal)

#MODIFICAR UN VALOR

salarioPersonal["Jose Maria"]=1200 # -> nombreDiccionario[claveDelValorModificar]= nuevoValor

print(salarioPersonal)

#ELIMINAR UN VALOR

del salarioPersonal["Mateo"] # -> del NombreDiccionario[claveAEliminar]

print(salarioPersonal)

#EJEMPLO DINAMICO DE DICCIONARIO
diccionario ={"España":"Madrid",
              "Vinicius Jr":7,
              "Poblacion": 28.5,
              "Liga": True}

print(diccionario)

#TUPLAS COMO CLAVE

futbolistasMadrid = ["Vinicius Jr", "Mbappe","Guler", "Rodrygo"]

diccionarioDorsales = {futbolistasMadrid[0]:7,
                       futbolistasMadrid[1]:10,
                       futbolistasMadrid[2]:15,
                       futbolistasMadrid[3]:21}


print(diccionarioDorsales)

#ACCESO A UNA CLAVE

print(diccionario["Vinicius Jr"])
print(diccionarioDorsales[futbolistasMadrid[2]])


#FUNCION KEYS

#SE USA PARA AVERIGUAR LAS CLAVES DE UN DICCIONARIO

print(diccionarioDorsales.keys()) # -> print(nombreDiccionario.keys())


#FUNCION VALUES

#INDICA EL VALOR DE LAS CLAVES

print(diccionarioDorsales.values()) # -> print(nombreDiccionario.values())

#LONGITUD DICCIONARIO

print(len(diccionarioDorsales)) # -> print(len(nombreDiccionario))

#DICCIONARIO ANIDADO

datosMbappe = {
    "DorsalesMbappe": {
        "DorsalesMonaco": [25, 39, 33, 29, 13, 11, 10],
        "DorsalesPSG": [9, 29, 14, 7, 17, 14, 7, 17, 7],
        "DorsalesMadrid": [9, 10]
    },
    "Nombre": "Kylian",
    "Apellido1": "Mbappé",
    "Apellido2": "Lottin",
    "Equipo": ["Real Madrid", "Paris Saint Germain", "AS Monaco"],
    "Titulos": {
        "AS Monaco" : [2017],
        "Paris Saint Germain" : [2018,2019,2020,2021,2022,2023,2024],
        "Real Madrid" : [2025],
        "Francia" : [2018,2021]
}}



print(datosMbappe)





