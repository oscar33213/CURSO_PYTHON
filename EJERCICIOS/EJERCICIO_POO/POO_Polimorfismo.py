#POLIMORMISMO

class Persona():
    def hablar(self):
        return "Hablo como una persona"
    
class Trabajador(Persona):
    def hablar(self):
        return "Hablo como un trabajador"
    
class Director (Trabajador):
    def hablar(self):
        return "Hablo como un director"
    
#EL POLIMORFISMO SE HACE VISIBLE EN EL OBJETO 'persona' VARIANDO SU COMPORTAMIENTO A LO LARGO DE LA EJECUCIÓN
def hazlosHablar(lista):
    for persona in lista:
        print(persona.hablar())
        

Antonio = Persona()
Mateo = Trabajador()
Julian = Director()

print(Antonio.hablar())
print(Mateo.hablar())
print(Julian.hablar())

print("-------------------------")

listaPersonas = [Antonio, Mateo, Julian]

hazlosHablar(listaPersonas)
