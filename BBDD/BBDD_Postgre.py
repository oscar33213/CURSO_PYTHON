# -*- coding: utf-8 -*-
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='PERSONAS',
    user='postgres',
    password='12345'
)

cur = conn.cursor()
cur.execute("SELECT version();")
print(cur.fetchone())

cur.close()
conn.close()


