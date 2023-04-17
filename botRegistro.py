import requests

datos = {
    'nombre': 'Leonel Macedo Mora', 
    'matricula': 'S18014114', 
    'carrera': 'Redes y Servicios de Cómputo', 
    'semestre': '9'
}

url = 'https://xl666.pythonanywhere.com/registro/'
res = requests.post(url, datos)

#for linea in open('archivo.txt'):