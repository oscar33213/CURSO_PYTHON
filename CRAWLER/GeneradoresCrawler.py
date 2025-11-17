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
        try:
            while urlAbsoluta != "":
                miDoc = requests.get(urlAbsoluta)
                docFinal = BeautifulSoup(miDoc.text, 'html.parser')
            
        
                for card in docFinal.select('.card'):
                    titulo = card.select('.card-title span')[1].text
                    emoticono = card.select_one('.emoji').text  
                    texto = card.select_one('.card-text').text 
                    imagen = urljoin(urlAbsoluta, card.select_one('img')['src'])
                    
                    #GENERADOR
                    yield CrawlerPost(emoticono, titulo, texto, imagen)
            
                    
                    
            
                web_siguiente = urljoin(urlAbsoluta, docFinal.select_one('.navigation .btn').attrs['href'])
                print(web_siguiente)
                
                urlAbsoluta = web_siguiente
                time.sleep(1)
        except AttributeError:
            print(f'Ultima pagina')
        
            

unPost = ExtratPost()
listaPost = unPost.extraerInfo()
for elPost in listaPost:
    
    print(elPost.emote)
    print(elPost.titulo)
    print(elPost.texto)
    print(elPost.imagen)
    print()
