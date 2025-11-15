import sys
from .USUARIOS.gestionusers import crearUser
from .PASSW.gestionContraseñas import CreatePswd

def crearDiccionarioUsuarios():
    usuarios_contraseñas = {}

    while True:
        print("\n--- Creación de usuario y contraseña ---")
        
        usuario = crearUser()
        contraseña = CreatePswd()

        # Guardamos en el diccionario
        usuarios_contraseñas[usuario] = contraseña
        print(f"Usuario '{usuario}' creado con su contraseña.")

        # Preguntamos si quiere seguir
        salir = input("¿Quieres añadir otro usuario? (s/n): ").lower()
        if salir == "n":
            print("\nDiccionario final de usuarios y contraseñas (contraseñas ocultas):")
            for user, pwd in usuarios_contraseñas.items():
                print(f"{user}: {'*' * len(pwd)}")  # 🔒 muestra la contraseña oculta
            sys.exit(0)

if __name__ == "__main__":
    crearDiccionarioUsuarios()

