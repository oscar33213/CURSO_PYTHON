from tkinter import *

#Raiz
raiz = Tk()
raiz.title("Tercera Ventana(Widget)")
raiz.resizable(1,1)
raiz.iconbitmap('D:\CURSO PYTHON TUTORIZADO\INTERFACES GRAFICAS\ICONOS\camara.ico')

#Frame
miFrame = Frame(raiz, width=500, height=500)
miFrame.pack(fill='both', expand= 1)
miFrame.config(bg='red')
miFrame.config(width='650', height='500')


#LabelTxt = Label(miFrame, text='Eres mu tonto', font='Arial', anchor='center', fg='blue' )

#EMPAQUETADO DEL LABEL

#LabelTxt.place(x = 10, y = 125)

#SIMPLIFIXAR EL LABEL (SOLO SE USARA SI NO S EVA A ALTERAR DURANTE LA EJECUCIÓN)

Label(miFrame, text='Hola', fg='blue', font=('Comic Sans MS', 20)).place(x=10, y=20)

miLogo = PhotoImage(file ='D:\CURSO PYTHON TUTORIZADO\INTERFACES GRAFICAS\IMG\carpetas.png')
Label(miFrame, image= miLogo).place(x=50, y=60)


#loop
raiz.mainloop()