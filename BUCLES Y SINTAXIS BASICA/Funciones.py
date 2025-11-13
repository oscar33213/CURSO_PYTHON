#FUNCIONES
import math

#FUNCION SIN ARGUMENTOS
def Area_Rectangulo():
    base = 20
    altura =10
    return(base*altura/2)

print (Area_Rectangulo())

#FUNCION CON ARGUMENTOS
def Area_Circulo(radio):
    
    return"El area del circulo con radio " + str(radio) + " es de: " + str((2*math.pi*radio**2))

#!SOLO UN RETURN EN UNA FUNCION


print(Area_Circulo(30))


def Imprimirvalores():
    print ("Hola")
    print("Adios")
    

Imprimirvalores()
print("Fin de programa")

#ALMACENAJE DE UNA FUNCION DENTRO DE UNA VARIABLE

areaCirculo = Area_Circulo(20)





