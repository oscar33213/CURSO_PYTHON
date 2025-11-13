#CONSTANTE
CONSTANTE = 1200 

beneficios = 200

print(CONSTANTE + beneficios)

#CONCATENACIÓN DE STRINGS
nombre = "Oscar"

edad = 28

ciudad = "Alcala De Henares"

print("Me llamo " + nombre + " " + "tengo " + str(edad) + " años" + " y soy de " + ciudad)

#str() CONVIERTE A STRING TODO LO CONTENIDO EN SUS PARENTESIS

#YTHON NO PERMITE CONCATENAR STRINGD CON OTRAS VARIABLRES (INT, FLOAT...)


salario = 1200

comision = salario + 100

print("Me llamo " + nombre + " " + "tengo " + str(edad) + " años" + " y soy de " + ciudad + " y mi sueldo es de " + str(salario + comision))

#LOS STRINGS DE MAS DE 1 LINEA SE COLOCAN DE LA SIGUIENTE MANERA:

cadenalarga = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged"""

print(cadenalarga)

