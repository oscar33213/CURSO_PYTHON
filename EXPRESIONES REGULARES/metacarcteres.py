import re

lista_nombres = ['Mateo Ruz',
                'Juan Hidalgo',
                'Pedro Pascal',
                'Luis Nuñez',
                'Pedro Perez',
                'Jorge Nitales',
                'Mateo Russo',
                'Nacho Hidalgo']

dominios = [
    "example.com",
    "google.com",
    "openai.com",
    "example.es",
    "github.com",
    "wikipedia.org",
    "elpais.es",
    "stackoverflow.com",
    "openai.es",
    "elpais.es"   
    ]

lista_terminos = [
    'Camión',
    'Camion',
    'Niños',
    'Niñas',
    'Ejemplo'
]
#META ^
for nombre in lista_nombres:
    if re.findall('^Pedro', nombre):
        print(nombre)
    else:
        print('No hay coincidencias')
        

for nombres in lista_nombres:
    if re.findall('o$', nombres):
        print(nombres)
    else:
        print('No hay coincidencias')

print('---------')

for dominio in dominios:
    if re.search('^e', dominio):
        print(dominio)
    else:
        print('No hay coincidencias')
        
print('--------')

for dominio in dominios:
    if re.search('.com$', dominio):
        print(dominio)
    else: 
        print('No hay coincidencias')


print('---------------------------------')

for lista in lista_terminos:
    if re.findall('cami[oó]n', lista.lower()):
        print(lista)
    else:
        print('No hay coincidencias')