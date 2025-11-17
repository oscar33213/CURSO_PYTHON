# 🕷️ Crawlers: Conceptos fundamentales y uso en Python

## 1. ¿Qué es un Crawler?

Un **crawler** (también llamado *araña*, *spider*, *indexador* o *rastreadores*) es un programa que:

- Analiza páginas web
- Examina su contenido
- Extrae información de forma automatizada

El término proviene del primer buscador web: **Web Crawler**.

---

## 2. ¿Para qué sirve un Crawler?

Los crawlers se utilizan para:

- Crear **bases de datos** con la información recolectada.
- Extraer principalmente **enlaces** (internos y externos) para continuar rastreando otras páginas.
- Construir estructuras en forma de **red** o *telaraña* con todo el contenido enlazado.

---

## 3. ¿Cómo funciona un Crawler?

1. El crawler accede a una página web.
2. Analiza los elementos HTML:  
   - Etiquetas  
   - Párrafos  
   - Tablas  
   - Enlaces  
3. Detecta los **enlaces** de la página.
4. Accede a las páginas enlazadas.
5. Repite el proceso de forma recursiva, expandiendo el rastreo.

Este proceso permite indexar grandes cantidades de información disponible en la web.

---

## 4. Python y los Crawlers

Python puede enviar **peticiones HTTP** y analizar contenido web gracias a librerías como:

- `requests` → obtiene la página web  
- `BeautifulSoup` → analiza su contenido

---

## 5. Ejemplo básico con `requests`

```python
import requests

miRequest = requests.get("https://www.marca.com/")

print(miRequest.status_code)  # 200 = respuesta correcta
print(miRequest.headers)      # Información de cabeceras
print(miRequest.text)         # HTML de la página

```

## Instalar la libreria request en python

- Instalamos request

```bash

pip3 install requests

```

- Una vez instalado, ya podemos trabajar con ella

## Beautiful Soap

- Para utilizarlo, hay que instalar su libreria

```bash

pip3 install BeautifulSoup4

```

- Uso de beayiful Soup

```python
from bs4 import BeautifulSoup

html_object = """""

    <html>
        <body>
            <p>Este es el primer parrafo </p>
            <p>Segundo parrafo </p>
            <a> Vinculo </a>
            
        </body>
    </html>
"""


docFinal = BeautifulSoup(html_object, "html.parser")

for parrafo in docFinal.find_all("p"):
    print(parrafo.text)
print("---ENLCES---")
for enlace in docFinal.find_all("a"):
    print(enlace.text)

```

## Localizar CSS

``` python

from bs4 import BeautifulSoup

html_object = """""

    <html>
        <style>
            .pImportante {
                color: red;
            }
        </style>
        <body>
            <p class='pImportante'>Este es el primer parrafo </p>
            <p>Segundo parrafo </p>
            <a> Vinculo </a>
            
        </body>
    </html>
"""

docFinal = BeautifulSoup(html_object, "html.parser")

for parrafo in docFinal.find_all("p"):
    print(parrafo.attrs) #BUSCA LOS TRAIBUTOS DE CLASE
    print(parrafo.text)

```

```python

#EJEMPLO REAL
html_object1 = requests.get("https://python.beispiel.programmierenlernen.io/")
print(html_object1.status_code)
docFinal_1 = BeautifulSoup(html_object1.text, "html.parser")
result = docFinal_1.select(".emoji")
print(result[4])
print(result[2].text)

```

## POO Crawler

- Uso de Crawler y BeatifulSoup con POO:

```python

import requests
from bs4 import BeautifulSoup

class CrawlerPost:
    def __init__(self, emoji, title, text, img):
        
        self.emote = emoji
        self.titulo = title
        self.texto = text
        self.imagen = img



class ExtratPost ():
    def extraerInfo(self):
        miDoc = requests.get('https://python.beispiel.programmierenlernen.io/')
        docFinal = BeautifulSoup(miDoc.text, 'html.parser')
        posts = []
        
        for card in docFinal.select('.card'):
            titulo = card.select('.card-title span')[1].text
            emoticono = card.select_one('.emoji').text  
            texto = card.select_one('.card-text').text 
            imagen = card.select_one('img').attrs       
            
            crawled = CrawlerPost(emoticono, titulo, texto, imagen) 
            posts.append(crawled)
            
        return posts
    
    
    
unPost = ExtratPost()
listaPost = unPost.extraerInfo()
for elPost in listaPost:
    print(elPost.emote)
    print(elPost.titulo)
    print(elPost.texto)
    print(elPost.imagen)
    print()

```

## Libreria urllib

- Sirve para obtener la ruta absoluta de una imagen

```python

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class CrawlerPost:
    def __init__(self, emoji, title, text, img):
        self.emote = emoji
        self.titulo = title
        self.texto = text
        self.imagen = img

class ExtratPost:
    def extraerInfo(self):
        urlAbsoluta = 'https://python.beispiel.programmierenlernen.io/' #DONDE SE ALMACENA LA URL_BASE
        miDoc = requests.get(urlAbsoluta)
        docFinal = BeautifulSoup(miDoc.text, 'html.parser')
        posts = []
        
        for card in docFinal.select('.card'):
            titulo = card.select('.card-title span')[1].text
            emoticono = card.select_one('.emoji').text  
            texto = card.select_one('.card-text').text 
            imagen = urljoin(urlAbsoluta, card.select_one('img')['src']) #urljoin, extarera la ruta absoluta
            
            crawled = CrawlerPost(emoticono, titulo, texto, imagen) 
            posts.append(crawled)
            
        return posts

unPost = ExtratPost()
listaPost = unPost.extraerInfo()

for elPost in listaPost:
    print(elPost.emote)
    print(elPost.titulo)
    print(elPost.texto)
    print(elPost.imagen)
    print()


```

## Archivos CSV

### Creación de CSV

- Un CSV en un documneto contenedor de grandes volumenes de información
- En este ejemplo, se crea un .csv a partir del objeto ***post*** del ejemplo de arriba

```python

import csv

with open('listasPosts.csv', 'w', newline='', encoding= 'utf-8') as csvfile:
    postwriter = csv.writer(csvfile, delimiter=';', #ESTE DELIMITADOR TRANSFORMA A COLUMNA UNA VEZ SE USE
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    for miPost in unPost.extraerInfo():
        postwriter.writerow([miPost.emote, miPost.titulo, miPost.texto, miPost.imagen])
    
```

- El codigo completo

```python

import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

class CrawlerPost:
    def __init__(self, emoji, title, text, img):
        self.emote = emoji
        self.titulo = title
        self.texto = text
        self.imagen = img

class ExtratPost:
    def extraerInfo(self):
        
        urlAbsoluta = 'https://python.beispiel.programmierenlernen.io/'
        posts = []
        try:
            while urlAbsoluta != "":
                miDoc = requests.get(urlAbsoluta)
                docFinal = BeautifulSoup(miDoc.text, 'html.parser')
            
        
                for card in docFinal.select('.card'):
                    titulo = card.select('.card-title span')[1].text
                    emoticono = card.select_one('.emoji').text  
                    texto = card.select_one('.card-text').text 
                    imagen = urljoin(urlAbsoluta, card.select_one('img')['src'])
            
                    crawled = CrawlerPost(emoticono, titulo, texto, imagen) 
                    posts.append(crawled)
            
                web_siguiente = urljoin(urlAbsoluta, docFinal.select_one('.navigation .btn').attrs['href'])
                print(web_siguiente)
                #AL LLEGAR A LA PRIMERA VUELTA DE BUCLE, LA RUTA ABSOLUTA DEBERA CAMBIAR A LA PAGINA 2 Y ASI SUCESIVAMENTE
                urlAbsoluta = web_siguiente
                time.sleep(1)
        except AttributeError:
            print(f'Ultima pagina')
        finally:
            return posts

unPost = ExtratPost()
listaPost = unPost.extraerInfo()

for elPost in listaPost:
    print(elPost.emote)
    print(elPost.titulo)
    print(elPost.texto)
    print(elPost.imagen)
    print()



with open('listasPosts.csv', 'w', newline='', encoding= 'utf-8') as csvfile:
    postwriter = csv.writer(csvfile, delimiter=';', #ESTE DELIMITADOR TRANSFORMA A COLUMNA UNA VEZ SE USE
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    for miPost in unPost.extraerInfo():
        postwriter.writerow([miPost.emote, miPost.titulo, miPost.texto, miPost.imagen])
    
        
        

```

### Lectura del CSV

- Este codigo, leera la información dentro de un **CSV**

```python

import csv

with open('listasPosts.csv', 'r', newline='', encoding= 'utf-8') as csvfile:
    postreader = csv.reader(csvfile, delimiter=';', 
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    for posts in postreader:
        print(', '.join(posts))
```
