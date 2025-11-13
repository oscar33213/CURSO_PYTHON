# 6) Número par o impar
def ejercicio_6_par_o_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
    
numeroAnalizar = float(input("Introduce un numero decimal: "))

numero = numeroAnalizar

print(ejercicio_6_par_o_impar(numero))