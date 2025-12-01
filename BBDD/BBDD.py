import sqlite3

#CREAR LA CONEXIÓN
miConexion = sqlite3.connect('D:\CURSO PYTHON TUTORIZADO\BBDD/miBase') 

#CREAR EL CURSOR
miCursor = miConexion.cursor()
#CONSULTA
miCursor.execute('SELECT* FROM PRODUCTOS')
listaProductos = miCursor.fetchall()

for p in listaProductos:
    print(f'Nombre: {p[0]}\nPrecio: {p[1]}€\nSección: {p[2]}.')
#CERRAR EL CURSOR
miCursor.close()

#CERRAR LA CONEXIÓN
miConexion.close()