import sqlite3

#CREAR LA CONEXIÓN
miConexion = sqlite3.connect('D:\CURSO PYTHON TUTORIZADO\BBDD/miBase') 

#CREAR EL CURSOR
miCursor = miConexion.cursor()

#CERRAR EL CURSOR
miCursor.close()

#CERRAR LA CONEXIÓN
miConexion.close()