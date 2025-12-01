def funcion_decoradora(funcion_parametro):
    def funcion_interna(*args, **kwargs):
        print("Voy a iniciar el calcúlo: ")
        
        funcion_parametro(*args, **kwargs)
        
        print("Trabajo finalizado...")
        
    return funcion_interna




@funcion_decoradora
def suma(num1, num2):
    print(num1 + num2)
    

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(1,2)
potencia(2,2)
#FUNCION CON CLAVE:VALOR
potencia(base=4, exponente=10)



