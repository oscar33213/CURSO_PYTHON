

import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='PERSONAS',
    user='postgres',
    password='12345'  # usa tu contraseña real
)

cur = conn.cursor()
cur.execute(
    "INSERT INTO alumnos (nombre, apellido1, apellido2, curso) VALUES (%s, %s, %s, %s)",
    ('ÓSCAR', 'HIDALGO', 'LÓPEZ', 'SEGUNDO')
)

conn.commit()
cur.close()
conn.close()
