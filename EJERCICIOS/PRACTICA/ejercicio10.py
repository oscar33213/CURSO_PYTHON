# 10) Acceso permitido
# Pide usuario y contraseña; permite acceso solo si coinciden con las predefinidas.
def ejercicio_10_acceso_permitido(pwd):
    masterpwd = "12345"
    if masterpwd == pwd:
        return True
    else:
        return False


youpwd = input("Indica la contraseña: ")

pwd = youpwd

print(ejercicio_10_acceso_permitido(pwd))