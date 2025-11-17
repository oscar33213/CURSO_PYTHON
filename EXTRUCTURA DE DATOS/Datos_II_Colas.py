import queue


# COLAS FIFO

miCola = queue.Queue()
#AÑADIR ELEMENTOS A LA COLA
miCola.put("Madrid")
miCola.put("Barcelona")
miCola.put("Valencia")

#SACAR UN ELEMENTO DE LA COLA
print(miCola.get())
#SACAR LOS DEMAS ELEMENTOS
print("Siguientes elementos: ")

for elemento in miCola.queue:
    print(elemento)
    
print('--------------')
# COLA LIFO

miCola_2 = queue.LifoQueue()
miCola_2.put("Madrid")
miCola_2.put("Barcelona")
miCola_2.put("Valencia")

print("Siguientes elementos: ")

for elemento in miCola_2.queue:
    print(elemento)
    
    

# COLAS PRIORITY

miCola_3 = queue.PriorityQueue()
miCola_3.put((3,"Madrid"))
miCola_3.put((2,"Barcelona"))
miCola_3.put((1, "Valencia"))


for elemento in miCola_3.queue:
    print(elemento)
    
    

cola = queue.Queue(4) #EL PARAMETRO INDICA QUE LA COLA SOLO TENDRA '4' ELEMENTOS
numero = 1
while not cola.full():
    cola.put(f'El numero es: {numero}')
    numero += 1

for elem in cola.queue:
    print(elem)
    

