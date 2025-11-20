from tkinter import *

raiz = Tk()
raiz.title("Segunda Ventana(Frame)")
raiz.resizable(1,1)
raiz.iconbitmap('D:\CURSO PYTHON TUTORIZADO\INTERFACES GRAFICAS\ICONOS\camara.ico')

#CREAR EL FRAME

miFrame = Frame()

#EMPAQUETADO DEL FRAME

miFrame.pack(fill='both', expand= 1)

#TAMAÑO DEL FRAME

miFrame.config(bg='red')

#TAMAÑO DEL FRAME

miFrame.config(width='650', height='500')































raiz.mainloop()
