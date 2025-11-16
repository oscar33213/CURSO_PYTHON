import requests



miRequest = requests.get("https://www.marca.com/")

print(miRequest.status_code) #SI DEVUELVE'200' A PROCESADO CORRECTAMENTE LA PETICIÓN
print(miRequest.headers)
print(miRequest.text)