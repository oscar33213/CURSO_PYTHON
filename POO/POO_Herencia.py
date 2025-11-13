#HERENCIA DE CLASES EN PYTHON
# UNA CLASE PUEDE HEREDAR PROPIEDADES Y METODOS DE OTRA CLASE
# LA CLASE QUE HEREDA SE LLAMA CLASE HIJA O SUBCLASE
# LA CLASE DE LA QUE SE HEREDA SE LLAMA CLASE PADRE O SUPERCLASE
# LA SUBCLASE PUEDE TENER SUS PROPIEDADES Y METODOS PROPIOS ADEMÁS DE LOS QUE HEREDA DE LA SUPERCLASE
# LA SUBCLASE PUEDE SOBRESCRIBIR METODOS DE LA SUPERCLASE SI ES NECESARIO


class Persona():
    def __init__(self, nombre, apellido, edad):
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def getDatosPersonales(self):
        return "Nombre: " + self.nombre + " .Apellido: " + self.apellido + " .Edad: " + str(self.edad) + " años."
    
    def habla(self):
        return self.nombre + " esta hablando"
    def piensa (self):
        return self.nombre + " esta pensando"
    def camina(self):
        return self.nombre + " esta caminando"
    def come(self):
        return self.nombre + " esta comiendo"
    
# CREACION DE LA SUBCLASE ESTUDIANTE QUE HEREDA DE LA CLASE PERSONA
# LA SUBCLASE PUEDE TENER SU PROPIO CONSTRUCTOR Y SUS PROPIOS METODOS
# PARA LLAMAR AL CONSTRUCTOR DE LA CLASE PADRE SE USA LA FUNCION SUPER()
# LA SUBCLASE PUEDE ACCEDER A LOS METODOS Y PROPIEDADES DE LA CLASE PADRE
# LA SUBCLASE PUEDE SOBRESCRIBIR METODOS DE LA CLASE PADRE SI ES NECESARIO
# EJEMPLO DE HERENCIA:
class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, escuela):
        self.escuela = escuela
        # Llamada al constructor de la clase base
        
        Persona.__init__(self, nombre, apellido, edad)
    def estudia(self):
        self.nombre + " esta estudiando"
        
    def getEstudio(self):
        return "El estudiante " + self.nombre + " estudia en la escuela " + self.escuela
    # Sobrescribir el método getDatosPersonales de la clase base
    def getDatosAlumno(self):
        return super().getDatosPersonales() + " Escuela: " + self.escuela
    

p1 = Estudiante("Oscar", "Hidalgo", 28, "CEU")



print(p1.getEstudio())
print(p1.getDatosAlumno())


#HERENCIA MULTIPLE
#CUANDO SE REALIZA UNA HERENCIA MULTIPLE, EL PARAMETRO super(). PASA A CONVERTIRSE EN LA CLASE PADRE QUE HEREDARA CADA UNA DE LAS CLASES DE LAS QUE VA A HEREDAR LA HERENCIA MULTIPLE
#EN EL CASO DE DIRECTOR, AL HEREDAR DE TRABAJADOR Y ESTUDIANTE, ESTE EN EL CONSTRUCTOR NO USARA super(). SI NO QUE USARA Trabajador. y Estudiante.
#AL HACER ESTO, AMBOS CONTRUCTORES DE TRABAJADOR Y ESTUDIANTE, DEBERAN MODIFICAR super(). POR Persona. YA QUE HEREDAN DE ESTA
#TODOS TODOS RECIBEN 'self' COMO PRIMER PARAMETRO


class Trabajador (Persona):
    def __init__(self, nombre, apellido, edad, trabajo, salario, puesto):
        self.trabajo = trabajo
        self.salario = salario
        self.puesto = puesto
        Persona.__init__(self, nombre, apellido, edad)

    def getDatosTrabajador(self):
        return super().getDatosPersonales() + " Lugar de trabajo: " + self.trabajo + " .Sueldo: " + str(self.salario) + " . Puesto de Trabajo: " + self.puesto + "."
    def Trabajo(self):
        return "El trabajador " + self.nombre + " esta trabajando de: " + self.trabajo
    #EL ORDEN EN LA QUE POSICIONES LA HERENCIA ES CRUCIAL, EL PRIMERO QUE AÑADES ES EL DE MAYOR PESO
class Director (Trabajador, Estudiante):
    def __init__(self, nombre, apellido, edad, trabajo, salario, puesto, empleadoscargo, escuela):
        self.empleados = empleadoscargo
        Trabajador.__init__(self, nombre, apellido, edad, trabajo, salario, puesto)
        Estudiante.__init__(self, nombre, apellido, edad, escuela)
    def dirige(self):
        return "El director de: " + self.trabajo + " se llama: " + self.nombre
    
    def getDatosDirector (self):
        return super().getDatosPersonales() + " tiene: " + str(self.empleados) + " trabajadores a su cargo"   
    def Estudio(self):
        return "El director de: " + self.trabajo + " estudia en: " + self.escuela + "."


p3 = Trabajador("Mateo", "Ruiz", 34,"Logistic", 1200, "Mozo de Almacén")
p4 = Director("Matias", "Ruiperez", 55, "Logistic", 2500, "CEO", 150, "UNIVERSAE")

print(p4.getDatosDirector())
print (p4.Estudio())