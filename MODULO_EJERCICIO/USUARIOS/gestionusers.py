import sys

def crearUser():
    while True:
        user = input("Añade el nombre de usuario: (salir para cerrar) ")
        if user.lower() == "salir":
            print("Saliendo del programa...")
            sys.exit(0)

        while len(user) < 5 or len(user) > 15 or not user.isalnum():
            print("Usuario inválido. Debe tener entre 5 y 15 caracteres y solo letras/números.")
            user = input("Añade el nombre de usuario: (salir para cerrar) ")
            if user.lower() == "salir":
                print("Saliendo del programa...")
                sys.exit(0)

        print(f"Usuario '{user}' creado correctamente.")
        return user   # 🔑 devuelve el usuario



