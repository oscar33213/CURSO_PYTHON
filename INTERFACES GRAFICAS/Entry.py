from tkinter import *

root = Tk()
root.title('Entry')
miFrame = Frame(root, height=800, width=1000)
miFrame.pack(fill='both', expand=1)
miFrame.config()

#CREAR EL ENTRY
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



































root.mainloop()