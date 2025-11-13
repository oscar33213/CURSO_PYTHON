#ARGUMENTOS INDEFINIDOS

#METODO __str__()

class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
#CON ESTE METODO HACEMOS QUE TODA LA INFORMACIÓN DEL OBJETO PASE A STRING   
    def __str__(self):
        return f"Datos de {self.nombre}: \nNombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad} "
        


p1 = Persona("Oscar", "Hidalgo", 28)


print(p1)

print("---------------------------")
#NUMERO ILMITADO DE PARAMETROS

class Trabajador:
    def __init__(self, *datos):
        self.almacenDatos = []
        for dato in datos:
            self.almacenDatos.append(dato)
            
    def __str__(self):
        return f"Datos de Trabajador: \nNombre: {self.almacenDatos[0]}\nApellido: {self.almacenDatos[1]}\nEdad: {self.almacenDatos[2]}"

p2 = Trabajador("Jose", "Martinez", 23)
print(p2)

print("---------------------------")

#USANDO GETTERS

class Estudiante:
    almacen_datos = []
    def __init__(self, *datos):
        for dato in datos:
            self.almacen_datos.append(dato)
        self.getDatos(self.almacen_datos)
        
    def getDatos(self, info):
        for dato in info:
            print(dato)
            
            
p3 = Estudiante("Pedro", "Duque", 23, "CEU")
print("----------------------------------")
#USANDO EL **
#EN ESTE CASO **datos AL LLEVAR DOS '*' VA A PEDIR UN DICCIONARIO (CLAVE:VALOR)
class Director:
    
    def __init__(self, **datos):
        elementos = datos.items()
        for clave, valor in elementos:
            print(clave, " -> ", valor)

            
#AL CREAR LA INSTANCIA AQUI SE INDICA {Clave:Valor}            
p4 = Director(Nombre = "Jorge", Apellido = "Perez", Edad = 28, Empresa = "Logitics", Sueldo = 2500)