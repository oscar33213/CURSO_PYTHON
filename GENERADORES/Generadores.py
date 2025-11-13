#GENERADORES

#ESTRUCTURAS PARECIDAS A FUNCIONES QUE DEVUELVEN VARIOS VALORES

# SE ALMACENAN EN OBJETOS ITERABLES (SE PUEDEN RECORRER)

# CADA VEZ QUE SE ALMACENA UN VALOR, ESTE PASA A ESTADO 'SUSPENSION DE ESTADO' HASTA QUE SE SOLICITA EL SIGUIENTE




#FUNCION
def CreaNumPares(limite):
    num = 1
    numPares = []
    
    while num < limite:
        numPares.append(num * 2)
        num += 1
    
    return numPares
    


#GENERADOR
print(CreaNumPares(20))


def GeneraNumPares(limite):
    numero = 1
    
    while numero < limite:
        yield numero * 2
        
        numero+= 1
        
listaPares = GeneraNumPares(30)


for i in listaPares:
    print(i)
    
    


