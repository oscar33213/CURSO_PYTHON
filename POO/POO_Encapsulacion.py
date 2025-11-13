#ENCAPSULACIÓN
edad = int(input("Indica tu edad: "))
class Persona ():
    #CON EL '_' INDICAS QUE A ESTOS PARAMETROS SOLO PUEDE ACCEDER ESTA CLASE Y LAS QUE HEREDEN
    _nombre = ""
    _apellido = ""
    __edad = 0
    __genero = "NO DEFINIDO" #AL AÑADIR 2 __ INDICAS QUE SOLO VAA PODER SER ACCESIBLE DENTRO DE ESTA CLASE
    
    def __init__(self, nombre, apellido, genero):
        self._nombre = nombre
        self._apellido = apellido
        self.__genero = genero
        
    #SETTER
    
    def setEdad(self, edadindicada):
        if edadindicada < 0 or edadindicada > 100:
            print ("EDAD NO PERMITIDA")
        else:
            self.__edad = edadindicada
            return self.__edad
        
    def habla(self):
        return self._nombre + " esta hablando"
    
    def camina (self):
        return self._nombre + " esta caminado"
    
    
    def getDatos (self):
        return "Nombre: " + self._nombre + ". " + " Apellido: " + self._apellido + ". " + " Edad: " + str(self.__edad) + " Genero: " + self.__genero + ". "
            
            


persona1 = Persona("Oscar", "Hidalgo", "Masculino") 
persona1.setEdad(edad)
print(persona1.getDatos())





