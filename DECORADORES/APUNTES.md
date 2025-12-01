# FUNCIONES DECORADORAS

## ¿QUE SON?

- Funciones que añaden **funcionalidad** a otras funciones

## ¿PARA QUE SIRVEN?

- Son utiles cuando hay que añadir ciertas funciones adicionales a un **numero indeterminado** de funciones
- Ayudan a facilitar a la hora de tener que **añadir** la misma funcionalidad extra a diversas funciones

## ¿COMO SE USA?

1. Se **construye** la funcionalidad en la **función decoradora**
2. Se **agrega** dicha funcionalidad a las funciones deseadas con la nomenclatura ***@nombref_decoradora*** previa a la funcion

## ESTRUCTURA

- Se basa en 3 funciones
- **Función A**, **Función B** y **Función C**.
  - **A** recibe como parametro a **B** y devuelve **C**
  - Una **función decoradora** siempre devuelve otra función
- Ejemplo:

```python

#FUNCION DECORADORA

def funcion_decoradora(funcion_parametro):
    def funcion_interna():
        print("Voy a iniciar el calcúlo: ")
        
        funcion_parametro()
        
        print("Trabajo finalizado...")
        
    return funcion_interna




@funcion_decoradora
def suma():
    print(25 + 30)


suma()

```

## FUNCION CON PARAMETROS

- Si una funcion recibe paarmetros, esta debera ser indicada en la **función decoradora**

```python

def funcion_decoradora(funcion_parametro):
    def funcion_interna(*args, **kwargs):
        print("Voy a iniciar el calcúlo: ")
        
        funcion_parametro(*args, **kwargs)
        
        print("Trabajo finalizado...")
        
    return funcion_interna




@funcion_decoradora
def suma(num1, num2):
    print(num1 + num2)
    

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(1,2)
potencia(2,2)
#FUNCION CON CLAVE:VALOR
potencia(base=4, exponente=10)


```
