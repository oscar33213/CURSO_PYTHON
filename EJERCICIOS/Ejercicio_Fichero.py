import os
from io import open

directorioActual = 'EJERCICIOS/clientes'

if os.path.exists(directorioActual):
    os.chdir('EJERCICIOS/clientes')
    with open('clientes.txt', 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        clientes = []
    for linea in lineas:
        campos = linea.split(';')
        
        cliente = {
            'Codigo': campos[0],
            'Nombre': campos[1],
            'Dirección': campos[2],
            'Población': campos[3],
            'Telefono': campos[4],
            'Responsable': campos[5].strip()
        }
        
        clientes.append(cliente)
        
    for c in clientes:
        print("Codigo Articulo= {} Nombre= {} Dirección= {} Población= {} Tfno= {} Responsable= {}"
            .format(c['Codigo'], c['Nombre'], c['Dirección'], c['Población'], c['Telefono'], c['Responsable']))

else:
    print('Ruta no encontrada')
