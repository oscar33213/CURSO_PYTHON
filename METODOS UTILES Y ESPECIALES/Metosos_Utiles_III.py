#METODO __repr__()
#IGUAL QUE EL METODO __str__() PERO MAS PRECISA AL DEVOLVER LA INFORMACIÓN
import datetime

class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def __repr__(self):
        return f"Datos de {self.nombre}: \nNombre: {self.nombre}\nApellido: {self.apellido}."
    
    


p1 = Persona("Oscar", "Hidalgo" )


print(p1)

#EJEMPLO DE USO DE 'repr'
hoy = datetime.date.today()

print(repr(hoy))


#METODO __len__()
#DEVUELVE LA LONGITUD DE UNA CADENA

class Agenda:
    def __init__(self,):
        self.miAgenda = {}
        
    def AgrgarDatos(self, nombre, telefono):
        self.miAgenda[nombre] = telefono
        
    def __len__(self):
        return len(self.miAgenda)
        


agenda1 = Agenda()


agenda1.AgrgarDatos("Oscar", "665149912")
agenda1.AgrgarDatos("Mateo", "667340099")

print("Tienes ",str(len(agenda1)) + " contactos en tu agenda")

