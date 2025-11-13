# 2) Conversión de tipos
# Pide un número decimal y muéstralo redondeado al entero más cercano.
def ejercicio_2_conversion_tipos(num):
    if num <= 5:
        return int(num)
    else:
        return int(num+1)
    
    

escribeNum = float(input("Introduce el numero con decimales: "))

num = escribeNum


print(ejercicio_2_conversion_tipos(num))

