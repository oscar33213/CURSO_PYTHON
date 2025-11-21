
'''
def Area_Triangulo():
    base = float(input('Indica la base: '))
    altura = float(input('Indica la altura: '))
    
    while base < 0 or altura < 0:
        print('Solo valores positivos')
        base = float(input('Indica la base: '))
        altura = float(input('Indica la altura: '))
    
    area = (base * altura) / 2
    return f'El resultado es: {area}'


print(Area_Triangulo())

'''
#FUNCION LAMBDA

area_triangulo = lambda base,altura:(base*altura/2) 

print(f'El area del Traingulo es: {area_triangulo(3,6)}')