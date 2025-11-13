#METODOS UTILES

#MANIPULACION DE CADENAS


nUsuario = input("Introduce el numero de usuario: ")

print("El usuario es: " + nUsuario.upper())


#EJEMPLO PRACTICO

edad = input("Indica tu edad: ")

while(edad.isdigit() == False):
    print("Solo valores numericos.")
    edad = input("Indica tu edad: ")
    

if(int(edad)< 18):
    print("Menor de edad")
else:
    print("Mayor de edad")