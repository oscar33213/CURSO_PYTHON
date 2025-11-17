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
        urlAbsoluta = 'https://python.beispiel.programmierenlernen.io/'
        miDoc = requests.get(urlAbsoluta)
        docFinal = BeautifulSoup(miDoc.text, 'html.parser')
        posts = []
        
        for card in docFinal.select('.card'):
            titulo = card.select('.card-title span')[1].text
            emoticono = card.select_one('.emoji').text  
            texto = card.select_one('.card-text').text 
            imagen = urljoin(urlAbsoluta, card.select_one('img')['src'])
            
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
