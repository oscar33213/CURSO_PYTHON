#CONTINUE
#UNA VEZ SE LEA ESTA INSTRUCCIÓN PASA A LA SIGUIENTE INSTRUCCIÓN ROMPIENDO EL BUCLE

nombre = "Oscar Hidalgo"

contaNombre = 0

for i in nombre:
    if i == " ":
        continue
    
    contaNombre += 1 #(contaNombre = contaNombre +1)
    
print(contaNombre)


#PASS
#SE USA PARA DEJAR PENDIENTE UNA INSTRUCCION QUE NO SE A TERMINADO DE DESARROLLAR

for i in nombre:
    pass

class Clase:
    pass



#ELSE

email = input("Introduce el email: ")
arroba = False
for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba = False
    


print(arroba)


