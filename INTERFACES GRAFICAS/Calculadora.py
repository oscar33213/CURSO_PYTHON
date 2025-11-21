from tkinter import *

# ---------------- Ventana principal ----------------
raiz = Tk()
raiz.title("Calculadora")
miFrame = Frame(raiz)
miFrame.pack(padx=8, pady=8)

# variables globales
operacion = ""
reset_pantalla = False
resultado = 0
num1 = 0
contador_resta = 0
contador_multi = 0
contador_divi = 0

# ------------- pantalla ---------------------------------------
numeroPantalla = StringVar()
pantalla = Entry(miFrame, textvariable=numeroPantalla, width=18, justify="right")
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=5)
pantalla.config(background="black", fg="#03f943")
numeroPantalla.set("0")

# --------- Permitir mover la ventana con el ratón ---------
def start_move(event):
    # guarda el offset del cursor respecto a la ventana
    raiz._drag_x = event.x
    raiz._drag_y = event.y

def on_move(event):
    # calcula nueva posición absoluta en la pantalla
    x = event.x_root - raiz._drag_x
    y = event.y_root - raiz._drag_y
    raiz.geometry(f"+{x}+{y}")

def stop_move(event):
    raiz._drag_x = None
    raiz._drag_y = None

# enlazar la pantalla para poder arrastrar la ventana desde ella
pantalla.bind("<ButtonPress-1>", start_move)
pantalla.bind("<B1-Motion>", on_move)
pantalla.bind("<ButtonRelease-1>", stop_move)

# ------------------- pulsaciones teclado --------------------------
def numeroPulsado(num):
    global operacion
    global reset_pantalla

    if reset_pantalla:
        numeroPantalla.set(num)
        reset_pantalla = False
    else:
        # si la pantalla tiene "0" y se pulsa un número, lo reemplazamos
        if numeroPantalla.get() == "0":
            numeroPantalla.set(num)
        else:
            numeroPantalla.set(numeroPantalla.get() + num)

# ----------------funcion suma----------------------------------
def suma(num):
    global operacion
    global resultado
    global reset_pantalla

    try:
        resultado += float(num)
    except:
        resultado += 0
    operacion = "suma"
    reset_pantalla = True
    numeroPantalla.set(str(resultado))

# ---------------funcion resta------------------------------
def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla

    if contador_resta == 0:
        try:
            num1 = float(num)
        except:
            num1 = 0.0
        resultado = num1
    else:
        if contador_resta == 1:
            resultado = num1 - float(num)
        else:
            resultado = float(resultado) - float(num)
        numeroPantalla.set(str(resultado))
        resultado = numeroPantalla.get()

    contador_resta = contador_resta + 1
    operacion = "resta"
    reset_pantalla = True

# -------------funcion multiplicacion---------------------
def multiplica(num):
    global operacion
    global resultado
    global num1
    global contador_multi
    global reset_pantalla

    if contador_multi == 0:
        try:
            num1 = float(num)
        except:
            num1 = 0.0
        resultado = num1
    else:
        if contador_multi == 1:
            resultado = num1 * float(num)
        else:
            resultado = float(resultado) * float(num)
        numeroPantalla.set(str(resultado))
        resultado = numeroPantalla.get()

    contador_multi = contador_multi + 1
    operacion = "multiplicacion"
    reset_pantalla = True

# -----------------funcion division---------------------
def divide(num):
    global operacion
    global resultado
    global num1
    global contador_divi
    global reset_pantalla

    if contador_divi == 0:
        try:
            num1 = float(num)
        except:
            num1 = 0.0
        resultado = num1
    else:
        try:
            if contador_divi == 1:
                resultado = num1 / float(num)
            else:
                resultado = float(resultado) / float(num)
            numeroPantalla.set(str(resultado))
            resultado = numeroPantalla.get()
        except ZeroDivisionError:
            numeroPantalla.set("Error")
            resultado = 0
            contador_divi = 0
            operacion = ""
            reset_pantalla = True
            return

    contador_divi = contador_divi + 1
    operacion = "division"
    reset_pantalla = True

# ----------------funcion el_resultado----------------
def el_resultado():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    global contador_divi

    try:
        current = float(numeroPantalla.get())
    except:
        current = 0.0

    if operacion == "suma":
        numeroPantalla.set(str(resultado + current))
        resultado = 0
    elif operacion == "resta":
        numeroPantalla.set(str(float(resultado) - current))
        resultado = 0
        contador_resta = 0
    elif operacion == "multiplicacion":
        numeroPantalla.set(str(float(resultado) * current))
        resultado = 0
        contador_multi = 0
    elif operacion == "division":
        try:
            numeroPantalla.set(str(float(resultado) / current))
        except ZeroDivisionError:
            numeroPantalla.set("Error")
        resultado = 0
        contador_divi = 0

# ------------------ funcion reiniciar pantalla y estados ----------------
def reiniciar_pantalla():
    global operacion, resultado, num1, contador_resta, contador_multi, contador_divi, reset_pantalla
    operacion = ""
    resultado = 0
    num1 = 0
    contador_resta = 0
    contador_multi = 0
    contador_divi = 0
    reset_pantalla = False
    numeroPantalla.set("0")

# -------------fila 1---------------------------------------------
boton7 = Button(miFrame, text="7", width=3, command=lambda: numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command=lambda: numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command=lambda: numeroPulsado("9"))
boton9.grid(row=2, column=3)

# Botón "C" al lado del 9 (columna 4)
botonReset = Button(miFrame, text="C", width=3, command=reiniciar_pantalla)
botonReset.grid(row=2, column=4)

# operador "/" en la columna 5
botonDiv = Button(miFrame, text="/", width=3, command=lambda: divide(numeroPantalla.get()))
botonDiv.grid(row=2, column=5)

# -------------fila 2---------------------------------------------
boton4 = Button(miFrame, text="4", width=3, command=lambda: numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command=lambda: numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command=lambda: numeroPulsado("6"))
boton6.grid(row=3, column=3)

# operador "x" en columna 5
botonMult = Button(miFrame, text="x", width=3, command=lambda: multiplica(numeroPantalla.get()))
botonMult.grid(row=3, column=5)

# -------------fila 3---------------------------------------------
boton1 = Button(miFrame, text="1", width=3, command=lambda: numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command=lambda: numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=3, command=lambda: numeroPulsado("3"))
boton3.grid(row=4, column=3)

# operador "-" en columna 5
botonRest = Button(miFrame, text="-", width=3, command=lambda: resta(numeroPantalla.get()))
botonRest.grid(row=4, column=5)

# -------------fila 4---------------------------------------------
boton0 = Button(miFrame, text="0", width=3, command=lambda: numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame, text=",", width=3, command=lambda: numeroPulsado("."))
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=3, command=lambda: el_resultado())
botonIgual.grid(row=5, column=3)

# operador "+" en columna 5
botonSum = Button(miFrame, text="+", width=3, command=lambda: suma(numeroPantalla.get()))
botonSum.grid(row=5, column=5)

# iniciar loop
raiz.mainloop()
