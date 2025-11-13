def cifrado_cesar_extendido(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        
        if 32 <= ord(caracter) <= 126:
            nuevo = (ord(caracter) - 32 + desplazamiento) % 95 + 32
            resultado += chr(nuevo)
        else:
            resultado += caracter  
    return resultado



print("=== CIFRADO CÉSAR EXTENDIDO ===")
opcion = input("¿Quieres cifrar o descifrar? (c/d): ").lower()

texto = input("Introduce el texto: ")
desplazamiento = int(input("Introduce el desplazamiento (por ejemplo, 5): "))

if opcion == "c":
    resultado = cifrado_cesar_extendido(texto, desplazamiento)
    print("\n🔐 Texto cifrado:", resultado)
elif opcion == "d":
    resultado = cifrado_cesar_extendido(texto, -desplazamiento)
    print("\n🔓 Texto descifrado:", resultado)
else:
    print("\n⚠️ Opción no válida. Usa 'c' para cifrar o 'd' para descifrar.")
