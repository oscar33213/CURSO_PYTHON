SSolar = 'Mercurio, Venus, Tierra, Marte, Jupiter, Saturno, Urano, Neptuno, Pluton'

# SET
planetas = set()



for planeta in SSolar.split(', '):  
    planetas.add(planeta)
    

print(planetas)


