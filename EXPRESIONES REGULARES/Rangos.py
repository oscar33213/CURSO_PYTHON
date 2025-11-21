import re
#RANGOS
lista_terminos = [
    'Camión',
    'Camion',
    'Niños',
    'Niñas',
    'Ejemplo'
]

lista_productos = [
        'Ma1',
        'Se-1',
        'Ma2',
        'Va.1',
        'Ca1',
        'Ma.3',
        'Ma4',
        'Se-2',
        'Se.A',
        'SeB',
        'Va2',
        'Se.C']

for lista in lista_terminos:
    if re.findall('[p-z]', lista.lower()):
        print(lista)
    else:
        print('No hay coincidencias')
        
print ('´´´´´´´´´´´´´´´´')
for lista in lista_terminos:
    if re.findall('^[a-j]', lista.lower()):
        print(lista)
    else:
        print('No hay coincidencias')

print('------------------------------------')

for producto in lista_productos:
    if re.findall('Ma[1-3]', producto, re.IGNORECASE):
        print(producto)
    else:
        print('No hay coincidencias')
print('--------------------')        
for producto in lista_productos:
    if re.findall('Se[0-2A-B]', producto, re.IGNORECASE):
        print(producto)
    else:
        print('No hay coincidencias')


print('------------')

for producto in lista_productos:
    if re.findall('Ma[.:]', producto, re.IGNORECASE):
        print(producto)
    else:
        print('No hay coincidencias')
        

