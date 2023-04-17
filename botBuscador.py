import requests
from bs4 import BeautifulSoup
import sys

URL = 'https://www.wordreference.com/definicion/' + sys.argv[1]

def recuperar_contenido(url=URL):
    try:
        res = requests.get(url)
        if not res.status_code == 200:
            return None
    except:
        return None
    return res.text

def parsear_palabra(html):
	soup = BeautifulSoup(html, 'html.parser')
	elementos = soup.find_all('ol', class_='entry')
	significado = elementos[0].text
	return significado

if __name__ == '__main__':
    texto = recuperar_contenido(URL)
    if not texto:
        print('La petición no se pudo realizar')
        exit(1)
    significado = parsear_palabra(texto)
    print(significado)

print(sys.argv[1])
