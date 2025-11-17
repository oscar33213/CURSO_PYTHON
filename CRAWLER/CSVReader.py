import csv

with open('listasPosts.csv', 'r', newline='', encoding= 'utf-8') as csvfile:
    postreader = csv.reader(csvfile, delimiter=';', 
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    for posts in postreader:
        print(', '.join(posts))
        
        
        
    
        
        
    