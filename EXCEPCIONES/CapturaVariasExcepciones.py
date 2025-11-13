
#CAPTURAR VARIAS EXCEPCIONES
import sys

def divide():
    contador = 0
    while True:
        try:
            op1 = (float(input("Introduce primer valor: ")))
            op2 = (float(input("Introduce segundo valor: ")))
            print("El resultado es: " + str(op1/op2))
            break
        except ZeroDivisionError:
            print("No se puede dividir por 0")
            print("Salida NO exitosa")
            sys.exit(1)
            
        except ValueError:
            print("El valor introducido no es numerico")
            contador = contador + 1
            if contador == 3:
                print("Limite de intentos sobrepasado. Finalizando programa")
                sys.exit(1)
            else:
                print("Contador: " + str(contador))
                
    


divide()

#OTRA FORMA DE CPATURAR VARIAS EXCEPCIONES
def divide2():
    
    while True:
        try:
            op1 = (float(input("Introduce primer valor: ")))
            op2 = (float(input("Introduce segundo valor: ")))
            print("El resultado es: " + str(op1/op2))
            break
        except:
            print("Ha ocurrido un error")
            
divide2()



#FINALLY
#UN TRY PUEDE ESTAR SOLO CON FINALLY, PERO NUNCA SOLO O EXCEPT O FINALLY

def divide3():
    
    while True:
        try:
            op1 = (float(input("Introduce primer valor: ")))
            op2 = (float(input("Introduce segundo valor: ")))
            print("El resultado es: " + str(op1/op2))
            break
        except:
            print("Ha ocurrido un error")
            
        finally:
            print("Esta linea siempre se va a ejecutar pase lo que pase")
        
            
divide3()
print("Calculo finalizado...")

