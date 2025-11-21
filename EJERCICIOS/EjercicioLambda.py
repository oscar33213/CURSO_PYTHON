
lista_ordenar = ['Los Lunes son los mejores dias para programar', 'Python es moderno', 'Veremos Inteligencia Artificial mas adelante', 'Lambda simplifica el codigo']

lista_ordenar.sort(key=lambda n: len(n.split()), reverse=True)


print(lista_ordenar)





