from tkinter import *
from tkinter import messagebox as Messagebox

root = Tk()
root.title("Boton")


miFrame = Frame(root, height=500, width=500)
miFrame.pack(fill='both', expand=1)
miVariable = StringVar()
paswdCuadro = Entry(miFrame, textvariable=miVariable)
paswdCuadro.grid(row=0, column=1, padx=5, pady=5)
paswdCuadro.config(show='X')

#OCULTAR CARACTERES

labelPswd = Label(miFrame, text='Contraseña: ')
labelPswd.grid(row=0, column=0, sticky='w')
#CUADRO DE TEXTO

#Input
CuadroAboutYou = Text(miFrame, width=15, height=8)
CuadroAboutYou.grid(row=1, column=1)

#BARRA DE DESPLAZAMIENTO

BarraDesplazamiento = Scrollbar(miFrame, command=CuadroAboutYou.yview) #Nombrevariable = Scroll(ContenedroPadre, command=VariableALaQueAfecta.y/xview)
BarraDesplazamiento.grid(row=1, column=2, sticky='nsew')
CuadroAboutYou.config(yscrollcommand=BarraDesplazamiento.set)
#Label
LabelCajaTexto = Label(miFrame, text='Sobre ti: ')
LabelCajaTexto.grid(row=1, column=0)


#BOTON

def funcionBoton():
    valor = miVariable.get()
    Messagebox.showinfo('Información' ,f'Contraseña: {valor}')

BotonEnviar = Button(miFrame, text='Enviar', width=17, command=funcionBoton)
BotonEnviar.grid(row=2, column=1, pady=5)

























root.mainloop()