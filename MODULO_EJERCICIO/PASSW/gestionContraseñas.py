import sys

def CreatePswd():
    while True:
        password = input("Indica tu contraseña: (salir para cerrar) ")
        if password.lower() == "salir":
            print("Finalizando el programa...")
            sys.exit(0)

        while len(password) < 10 or not any(char.isdigit() for char in password) or password.isalnum():
            print("Contraseña inválida. Debe tener más de 10 caracteres, al menos un número y un carácter especial.")
            password = input("Indica tu contraseña: (salir para cerrar) ")
            if password.lower() == "salir":
                print("Finalizando el programa...")
                sys.exit(0)

        print(f"Contraseña '{password}' creada correctamente.")
        return password   # 🔑 devuelve la contraseña




