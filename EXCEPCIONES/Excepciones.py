# EXCEPCIONES
# ERRORES EN TIEMPOS DE EJEUCIÓN
import sys
contador = 0
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2
#CAPTURA DE EXCEPCIONES:
def divide(num1, num2):
    try: #PARTE DEL CODIGO QUE ES SUPSCEPTIBLE A ERROR
        return num1 / num2
    except ZeroDivisionError: #LO QUE EL PROGRAMA HARA EN CASO DE ERROR (SE DEBE COLOCAR EL ERROR QUE LANZA EN CONSOLA)
        print("No se puede dividir por 0")
        return "Fallo en la operación"

while True:
    try:
        op1 = int(input("Introduce el primer número: "))
        op2 = int(input("Introduce el segundo número: "))
        break
    except ValueError:
        print("Solo valores numéricos")
        if contador == 2:
            print("Finalizando el programa")
            sys.exit(1)
        else:
            contador = contador + 1
            print("Contador:" + str(contador))


    

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecución del programa ")