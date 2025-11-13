#GENERADORES II
#YIELD FROM

def CapitalesMundo(*ciudades): #el * indica que el numero d eparametros que va a recibir la funcion es indeterminado y lo añede a un tupla
    for capital in ciudades:
        yield from capital
        
        
        


capitalesVueltas = CapitalesMundo("Madrd" , "Pekin", "Roma", "Brujas")


print(next(capitalesVueltas))
print(next(capitalesVueltas))
print(next(capitalesVueltas))
print(next(capitalesVueltas))


