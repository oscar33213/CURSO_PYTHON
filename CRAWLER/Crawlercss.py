from bs4 import BeautifulSoup
import requests
#EJEMPLO BASICO
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
    print(parrafo.attrs)
    print(parrafo.text)

    
print("----EJEMPLO REAL----")

#EJEMPLO REAL
html_object1 = requests.get("https://python.beispiel.programmierenlernen.io/")
print(html_object1.status_code)
docFinal_1 = BeautifulSoup(html_object1.text, "html.parser")
result = docFinal_1.select(".emoji")
print(result[4])
print(result[2].text)





