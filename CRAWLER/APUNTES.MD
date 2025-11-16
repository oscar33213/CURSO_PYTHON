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
