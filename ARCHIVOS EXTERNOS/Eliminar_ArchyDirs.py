import os

directorio = "Prueba"
archivo = os.path.join(directorio, "Prueba.txt")

if os.path.exists(directorio):
    if not os.listdir(directorio):  # está vacío
        os.rmdir(directorio)
        print(f"Directorio '{directorio}' eliminado porque estaba vacío.")
    else:  # no está vacío
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"Archivo 'texto.txt' eliminado dentro de '{directorio}'.")
        else:
            print("El archivo 'texto.txt' no existe dentro del directorio.")
else:
    print(f"El directorio '{directorio}' no existe.")