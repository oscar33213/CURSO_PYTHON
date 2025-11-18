import os
from io import open

directorioActual = 'EJERCICIOS/clientes'

# Verifica si existe el directorio 'EJERCICIOS/clientes'
if os.path.exists(directorioActual):
    # Cambia el directorio de trabajo al especificado
    os.chdir('EJERCICIOS/clientes')
    
    # Abre el archivo 'clientes.txt' en modo lectura con codificación UTF-8
    with open('clientes.txt', 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()  # Lee todas las líneas del archivo
        clientes = []  # Lista vacía para almacenar los clientes
        
        # Recorre cada línea del archivo
        for linea in lineas:
            campos = linea.split(';')  # Divide la línea en campos separados por ';'
            
            # Crea un diccionario con los datos del cliente
            cliente = {
                'Codigo': campos[0],
                'Nombre': campos[1],
                'Dirección': campos[2],
                'Población': campos[3],
                'Telefono': campos[4],
                'Responsable': campos[5].strip()  # Elimina espacios/saltos de línea
            }
            
            clientes.append(cliente)  # Añade el cliente a la lista
        
        # Recorre la lista de clientes y muestra sus datos formateados
        for c in clientes:
            print("Codigo Articulo= {} Nombre= {} Dirección= {} Población= {} Tfno= {} Responsable= {}"
                .format(c['Codigo'], c['Nombre'], c['Dirección'], c['Población'], c['Telefono'], c['Responsable']))

# Si no existe el directorio, lo crea
else:
    os.mkdir(directorioActual)


