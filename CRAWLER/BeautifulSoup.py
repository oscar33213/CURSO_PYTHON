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