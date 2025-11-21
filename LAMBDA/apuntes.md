# FUNCIONES LAMBDA

---

## ¿Qué son?

- Son funciones anonimas; es decir, funciones que no tienen nombre

---

## ¿Para qué sirven?

- Sirven para **reducir**, **simplificar** y **abreviar** el codigo en **determinados escenarios**

---

## ¿Cuando se pueden usar?

- Cuando vayamos a utilizar **funciones sencillas** de manera **repetida**
- Todo lo qeu hagamos con las **funciones lambda** se puede hacer con una **funcion normal** pero **NO** a la inversa
- Se les conoce como: **on the go**, **on demand**

---

## Usos

### Funcion regular

```python

def Area_Triangulo():
    base = float(input('Indica la base: '))
    altura = float(input('Indica la altura: '))
    
    while base < 0 or altura < 0:
        print('Solo valores positivos')
        base = float(input('Indica la base: '))
        altura = float(input('Indica la altura: '))
    
    area = (base * altura) / 2
    return f'El resultado es: {area}'

```

### Funcion Lambda

```python

area_triangulo = lambda base,altura:(base*altura/2) 
print(f'El area del Traingulo es: {area_triangulo(3,6)}')

```

- Uso de **lambda** en diferentes contextos:

```python

comision_formato = lambda comision: '¡{}!€'.format(comision)
comision1 = 5700
print(f'Antonio a tenido una comision de: {comision_formato(comision1)}')

```

- La expresión *(('¡{}!€'.format(var)))* añade al resultado, lo indicado
- **comision1 = 5700**
- **Resulatdo**: ¡5700€!

---

### Trabajo con Listas y Tuplas

- En este caso vamos a ver como se ordena una lista con tuplas de menor a mayor segun los resultados de la suma entre ellos

```python

lista_num = [(5,3),(9,26),(32,15),(21,46)]

def ordena_lista(t):
    return t[0] + t[1]

lista_num.sort(key=ordena_lista)

```

- Se le indica una lista con grupos de tuplas
- La funcion *normal* indica que devuleva el resulatdo de la suma entre tuplas
- Usando el metodo *.sort* se le indica como *key* la funcion

### Ejemplo con Lambda

- La misma funcion pero usando *lambda*

```python

lista_num = [(5,3),(9,26),(32,15),(21,46)]
(lista_num.sort(key=lambda t: t[0]+ t[1]))
print(lista_num)

```

```python

lista_musico = ['Paul McCartney', 'Bruce Springsteen', 'Bon Jovi', 'Jason Derulo', 'Freddie Mercury']

#Funcion Normal

def ordenar_musico(m):
    return m.split()[1]

lista_musico.sort(key=ordenar_musico)

print(lista_musico)

#Funcion Lambda

(lista_musico.sort(key=lambda m: m.split()[1]))
print(lista_musico)

```
