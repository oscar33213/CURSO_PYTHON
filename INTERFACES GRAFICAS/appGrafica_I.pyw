from tkinter import *

# CREAMOS LA RAIZ

raiz = Tk()
#MODIFICAR EL TITULO
raiz.title("Primera Ventana")
#MODIFICAR REDIMENSIONADO
raiz.resizable(1,1) #(0,0) no se redimensiona nada / (0,1) Solo el ancho / (1,0) Solo el largo / (1,1) Sin restriccion de redimensionado
##CAMBIO DE ICONO
raiz.iconbitmap('D:\CURSO PYTHON TUTORIZADO\INTERFACES GRAFICAS\ICONOS\camara.ico')
#MODIFICAR ESCALADO
raiz.geometry('1920x1080')
# MODIFICAR EL COLOR DE BACKGROUD
raiz.config(bg='blue')
raiz.mainloop() #BUCLE INFINITO QUE HARA QUE LA VENTANA SIEMPRE SE EJECUTE



