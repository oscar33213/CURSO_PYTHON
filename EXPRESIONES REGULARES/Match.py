import re

nombre1 = 'Lionel Messi'
nombre2 = 'Kylian Mbappé'
nombre3 = 'Zlatan Ibrahiovic'
nombre4 = 'Kylian Émbappé'

#MATCH
if re.match('Kylian', nombre1, re.IGNORECASE):
    print(f'Esta en el 1º')
elif re.match('Kylian', nombre2, re.IGNORECASE):
    print('Esta en el 2º')
elif re.match('Kylian', nombre3, re.IGNORECASE):
    print('Esrta en el 3º')
else:
    print('No esta')
    

print('--------')

if re.search(r'.lian', nombre1, re.IGNORECASE):
    print('Hay coincidencia en nombre1')
elif re.search(r'.lian', nombre2, re.IGNORECASE):
    print('Hay coincidencia en nombre2')
elif re.search(r'.lian', nombre3, re.IGNORECASE):
    print('Hay coincidencia en nombre3')
elif re.search(r'.lian', nombre4, re.IGNORECASE):
    print('Hay coincidencia en nombre4')
else:
    print('No hay coincidencia')


#Search

if re.search('L', nombre1, re.IGNORECASE):
    print(True, f'{nombre1}')
else:
    print(False)
