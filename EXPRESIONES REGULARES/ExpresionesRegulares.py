import re


cadena = 'Estoy trabajando con Python en Domingo y Semana Santa'


busqueda = 'Domingo'


if re.search(busqueda.lower(), cadena.lower()) is not None:
    print(f'Se encontro el {busqueda}')
else:
    print('No se encontro')