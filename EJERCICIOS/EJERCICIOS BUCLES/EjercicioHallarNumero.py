import random
print("Vamos a hallar el numero que estoy pensando")

numeroPensado = random.randint(0,100)

numeroElegido = (int(input("Elige un numero del 0 al 100: ")))

intentos = 0

while intentos < 10:
    if numeroElegido < 0 or numeroElegido > 100:
        print("Solo valores en el rango")
        intentos = intentos + 1
        print("Numero de intentos: " + str(intentos))
        numeroElegido = (int(input("Elige un numero del 0 al 100: ")))
        
    else:
        
        if numeroElegido != numeroPensado:
            print("NO ES EL NUMERO")
            intentos = intentos + 1
            print("Numero de intentos: " + str(intentos))
            numeroElegido = (int(input("Elige un numero del 0 al 100: ")))
        else:
            print("ES EL NUMERO")
            break
        



if numeroElegido == numeroPensado:
    if intentos < 3:
        print("Enhorabuena, lo has sacado en " + str(intentos) + " intentos. Estas hecho un fiera")
    elif intentos > 3 and intentos < 5:
        print("Bueno...lo has logardo en:" + str(intentos) + " intentos. Hay que mejorar")
    elif intentos > 5 and intentos < 8:
        print("Casi al limite eh, lo has logardo en: " + str(intentos) + " intentos... Muy mejorable")
    elif intentos == 9 :
        print("MADREMIA!!! NECESITAS MAS SUERTE, lo has logrado en:" + str(intentos) + " Intentos, casi al filo")
    
else:
    print("Oh has consumido los intentos, el numero era: " + str(numeroPensado))




