# Crea un programa que pregunte por consola la renta. En función de la renta introducida, el programa devolverá el texto: “A la renta (aquí iría la renta introducida) le corresponde un (aquí iría el tipo impositivo) de tipo impositivo.




renta = (float(input("Introduce tu nomina: ")))


if renta == 12000 and renta <= 18000:
    print("Tu renta de: " + str(renta) + " tiene un tipo Impositivo del 15%")
elif renta > 18000 and renta <= 35000:
    print("Tu renta de: " + str(renta) + " tiene un tipo Impositivo del 21 %")
elif renta > 35000 and renta <= 70000 :
    print("Tu renta de: " + str(renta) + " tiene un tipo Impositivo del 35 %")
elif renta < 12000:
    print("Tu renta de: " + str(renta) + " tiene un tipo Impositivo del 7%")
    
else:
    "Renta no admitida"
    




