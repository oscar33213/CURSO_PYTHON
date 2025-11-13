#CONDICIONAL IF

salario = 2000

if salario > 1000:
    print("Hola")
else:
    print("Adios")
    

#FUNCION CON CONDICIONAL DENTRO
def EvaluarNotas(notaAlumno):
    valoracion = ""
    if notaAlumno < 7:
        valoracion ="SUSPENSO"
    else :
        valoracion="APROBADO"
    return valoracion    

print(EvaluarNotas(8))
#INTRODUCIR DARTOS POR CONSOLA
notas = int(input("Indica al nota: "))
print(EvaluarNotas(notas))


#IF-ELSE IF

def NotasAlumno(notas):
    valoracion = ""
    
    if notas > 5 and notas <= 7:
        valoracion = "SUFICIENTE"
    elif notas > 7 and notas <= 9 :
        valoracion = "NOTABLE"
    elif notas < 5 :
        valoracion = "SUSPENSO"
    else:
        valoracion = "MATRICULA"
        
    return valoracion


introducirNota = int(input("Indica la nota del alumno: "))


print(NotasAlumno(introducirNota))









