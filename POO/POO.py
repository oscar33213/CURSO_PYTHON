
#CREACION DE CLASE
class Coche():
    #PROPIEDADES DE LA CLASE
    ruedas = 4
    largoChasis = 260
    anchoChasis = 130
    arrancado = False
    #COMPORTAMIENTO DE LA CLASE (ESTO NO ES OBLIGATORIO)
    def arrancaCoche(self): #POR OBLIGACIÓN LOS METODOS RECIBEN EL PARAMETRO 'self'
        #'self' ES EL OBJETO!
        self.arrancado = True
    
    def estadoCoche(self):
        if self.arrancado == True:
            return "El coche esta arrancado"
        else:
            return "El coche esta parado"
    
    
#CREACION DE OBJETO (INSTANCIA A LA CLASE)

mazda = Coche() #EJEMPLAR DE CLASE
renault = Coche()

print("El Renault tiene " + str(renault.ruedas) + " ruedas")
#LLAMAR A UN METODO
mazda.arrancaCoche()
print(mazda.estadoCoche())






