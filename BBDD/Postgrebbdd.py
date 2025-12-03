

import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='PERSONAS',
    user='postgres',
    password='12345'  
)

cur = conn.cursor()
cur.execute('SELECT* FROM ALUMNOS')

registros = cur.fetchall()

for p in registros:
    print(
        f'Nombre: {p[1]}\n'
        f'Primer Apellido: {p[2]}\n'
        f'Segundo Apellido: {p[3]}\n'
        f'Curso: {p[4]}.\n'
    )

conn.commit()
cur.close()
conn.close()
