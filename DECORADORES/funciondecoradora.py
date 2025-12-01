#FUNCION DECORADORA

def funcion_decoradora(funcion_parametro):
    def funcion_interna():
        print("Voy a iniciar el calcúlo: ")
        
        funcion_parametro()
        
        print("Trabajo finalizado...")
        
    return funcion_interna




@funcion_decoradora
def suma():
    print(25 + 30)


suma()


