#BUCLE WHILE
import math
n = 0

while n < 100:
    if n % 2 == 0:
        print (n)
    else :
        print("Papaya")
    n = n + 1



edad = int(input("Introduce tu edad: "))

#OR
while edad < 0 or edad > 100 :
    print("Edad no valida")
    edad = int(input("Introduce tu edad: "))

print("Puede pasar")


print("Vamos a buscar la raiz cuadrada")
valorNumerico = int(input("Indica un numero POSITIVO: "))

intentos = 0

while valorNumerico < 0 :
    if intentos > 3:
        print("Has superado el limite de intentos")
        break
    valorNumerico = int(input("Indica un numero POSITIVO: "))
    if valorNumerico < 0:
        print("SOLO VALORES POSITIVOS")
        
        
    
    intentos = intentos + 1
    
    
    

if valorNumerico >= 0:
    print ("La raiz cuadrada de: " + str(valorNumerico) + " es: " + str(math.sqrt(valorNumerico)))


