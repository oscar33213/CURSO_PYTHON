import re

cadena = 'Estoy trabajando con Python en Domingo y Semana Santa. El proximo Domingo no pienso estudiar'
busqueda = 'domingo'

texto_encontrado = re.search(busqueda, cadena, re.IGNORECASE)

print(texto_encontrado.start())
print(texto_encontrado.end())
print(texto_encontrado.span())


# FIND ALL

print(re.findall(busqueda, cadena, re.IGNORECASE))

#CONTRA LAS VECES QUE APARECE
veces_apear = (len(re.findall(busqueda, cadena, re.IGNORECASE)))

print(f'La palabra {busqueda.capitalize()} aparece: {veces_apear} veces')