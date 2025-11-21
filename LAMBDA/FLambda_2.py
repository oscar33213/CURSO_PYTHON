
import math


numero_elevado = lambda base, exponente: (base ** exponente)

print(numero_elevado(4,2))



comision_formato = lambda comision: '¡{}!€'.format(comision)


comision1 = 5700

print(f'Antonio a tenido una comision de: {comision_formato(comision1)}')


lista_num = [(5,3),(9,26),(32,15),(21,46)]
'''
def ordena_lista(t):
    return t[0] + t[1]
'''
(lista_num.sort(key=lambda t: t[0]+ t[1]))
print(lista_num)


lista_musico = ['Paul McCartney', 'Bruce Springsteen', 'Bon Jovi', 'Jason Derulo', 'Freddie Mercury']

#Funcion Normal

def ordenar_musico(m):
    return m.split()[1]

lista_musico.sort(key=ordenar_musico)

print(lista_musico)

#Funcion Lambda

(lista_musico.sort(key=lambda m: m.split()[1]))
print(lista_musico)