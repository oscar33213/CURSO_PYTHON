import requests
from bs4 import BeautifulSoup

htmldoc = requests.get("https://python.beispiel.programmierenlernen.io/")
docFinal = BeautifulSoup(htmldoc.text, "html.parser")

# Obtener todos los textos de los spans
spans = [s.text for s in docFinal.find_all("span")]

# Obtener los textos de card-text
textHTML = docFinal.select(".card-text")

# Obtener imágenes con ambas clases
imageHTML = docFinal.select(".card-block img")

# Imprimir resultados
print("SPANS:")
for s in spans:
    print("-", s)

print("\nTEXTOS card-text:")
for t in textHTML:
    print("-", t.text.strip())

print("\nIMÁGENES:")
for img in imageHTML:
    print("-", img.attrs["src"])
