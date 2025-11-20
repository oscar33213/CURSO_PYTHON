# INTERFACES GRAFICAS

## ¿Que es una Aplicación Grafica?

- Una aplicacion grafica es el programa que se construye con ventanas
- La aplicaciones se dividen en **tres grandes grupos**

  - **Consola**: Son las que se ejecutan en una consola de comandos
  - **Graficas**: Son las que se constituyen por ventanas
  - **Web**: Se requiere un navegador web para interactuar

- Tambien se denominan ***GUI*** (**G**RAFIC **U**SER **I**NTERFACE)
- Son intermediadores entre el programa y el usuario
- El usuario ve la parte de **botones**, **ventanas**, **cuadros de texto** ***(El Front - End)***
- El programa por detras ejecuta la **logica** ***(El Back - End)***
- Se usan diferentes librerias, aunque la mas conocida es **Tkinter**
  - *WxPython*
  - *PyQT*
  - *PyGTK*
  - *Etc...*

- **Tkinter** es el puente entre **Python** y la libreria **TCL/TK**

## Estructura de ventana

- **RAIZ** = Es el elemento principal, el contenedor de toda la interfaz
- **FRAME** = Espacio donde se colocaran los elementos (Botones, menús...)
- **WIDGET** = Cada uno d elos elementos que se colocan sobre el *frame*

## Creación de una Interfaz Grafica

- Primero comprobaremos si tenemos instalado **Tkinter** (Por defecto, Python la lleva)

```bash

python -m tkinter

```

- Si esta instalado, aparecera una ventana emergente contruida con Tkinter
- En caso de no estar instaldo, debereis instalarlo desde su pagina oficial.

### WINDOWS

1. descargar Python (o reinstalar) desde la web oficial

2. Durante la instalación marcar **tcl/tk**

3. Volver a ejecutar el comando de comprobación

### LINUX (UBUNTU/DEBIAN)

- Se instala por separado

```bash

sudo apt update
sudo apt install python3-tk

```

### MAC OS

- Como WIndows, veine instalado una vez descargas **Python** pero si no fuese el caso, ejecutariamos:

```bash

brew install python-tk

```

- Una vez comprobado, podemos pasar a su construcción

```python

from tkinter import *

# CREAMOS LA RAIZ
raiz = Tk()
#MODIFICAR EL TITULO
raiz.title("Primera Ventana")
#MODIFICAR REDIMENSIONADO
raiz.resizable(1,1) #(0,0) no se redimensiona nada / (0,1) Solo el ancho / (1,0) Solo el largo / (1,1) Sin restriccion de redimensionado
##CAMBIO DE ICONO
raiz.iconbitmap('Aqui ira la Ruta (Tanto absoluta como relativa)') 
#MODIFICAR ESCALADO
raiz.geometry('1920x1080')
# MODIFICAR EL COLOR DE BACKGROUD
raiz.config(bg='blue')
raiz.mainloop() #BUCLE INFINITO QUE HARA QUE LA VENTANA SIEMPRE SE EJECUTE (A DE ESTAR SIEMPRE AL FINAL)

```

- Podemos abrir la interfaz sin necesidad de hacerlo desd eel editor, dando doble *click* en el archivo desde el **Explorador de Archivos**, pero esto abrira una ventana *cmd* por detras

- Para quitar la *cmd* simplemente se cambia la extension *.py* a *.pyw* (**OJO** Es necesario tener habilitado la extension para archivo de tipo conocido)

## El Frame

```python
from tkinter import *
raiz  = Tk()
#CREAR EL FRAME
miFrame = Frame(raiz, width=500, height=500)
#EMPAQUETADO DEL FRAME
miFrame.pack(fill='both', expand= 1)
raiz.mainloop()

```

- Por defecto el Frame no cuenta con tamaño, para ello se le debera de dar

```python

miFrame.config(width='650', height='500')

```

## Widgets

- Para construir el widget primero crearemos el objeto **Label**

```python

miLabel = Label()

```

- Como parametros podra recibir:
  - **Text**: Texto que se muestra en el label
  - **Anchor**: Controla la posicion del texto
  - **Bg***: Color del fondo
  - **Bitmap**: Mapa de **bits** que se mostraran como grafico
  - **Bd**: Grosor del borde
  - **Font**: Tipo de fuente
  - **Fg**: Color de la fuente
  - **Width**: Ancho en caracteres
  - **Height**: Alto en caracteres
  - **Image**: Muestra imagenes en lugar de texto
  - **Justify**: Justifica el texto

```python

from tkinter import *

root = Tk()
miFrame.pack(fill='both', expand= 1)
LabelTxt = Label(miFrame, text='Eres mu tonto', font='Arial', anchor='center', fg='blue' )
LabelTxt.place(x = 10, y = 125)
raiz.mainloop()

```

- Ejemplo de crear un Label, mas simple
- Crearlo de esta manera hace que no se pueda modificar en tiempo de ejecución

```python

Label(miFrame, text='Hola').place(x=10, y=20)

```

## Colocar una imagen

```python

miLogo = PhotoImage(file='rutaImagen')
Label(miFrame, image= miLogo).place(x=50, y=60)

```

## Entry (Cuadro de texto)

- Se usa para escribir texto

```python

#CREAR EL ENTRY
cuadroTexto = Entry(miFrame)
cuadroTexto.place(x = 120, y= 110)

```

## GRID

- Divide el **Frame** en una cuadricula situando filas y columnas

```python

cuadroTexto.grid(row=0, column=1)

```

### EJEMPLO DE CREACIÓN COMPLETA DE UNA VENTANA ESTILO FORMULARIO

```python
from tkinter import *

root = Tk()
root.title('Entry')
miFrame = Frame(root, height=800, width=1000)
miFrame.pack(fill='both', expand=1)
miFrame.config()


cuadroTexto = Entry(miFrame)
cuadroTexto.grid(row=0, column=1)
cuadro2 = Entry(miFrame)
cuadro2.grid(row=1, column=1)
cuadro3 = Entry(miFrame)
cuadro3.grid(row=2, column=1)


miLabel = Label(miFrame, text='Nombre: ')
miLabel.grid(row=0,column=0, sticky='w')
miLabel2 = Label(miFrame, text='Apellido: ')
miLabel2.grid(row=1, column=0, sticky='w')
miLabel3 = Label(miFrame, text='Telefono de Contacto: ')
miLabel3.grid(row=2, column=0, sticky='w')

```

- En este codigo se crea un aplicacion con 3 entradas de texto
