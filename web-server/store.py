# Modulo que permite interactuar con servidores web
import requests

url = 'https://api.escuelajs.co/api/v1/products'
response = requests.get(url)

# Definición de función para solicitar las categorias
def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    # print(r.status_code) # 200 code reequest success
    # print(r.text) # return string
    # print(type(r.text)) # <class 'str'>
    categories = r.json() # convert string to json
    # print(categories) # return json
    for category in categories:
        print(category['name'])

# Definición de función para solicitar los productos
def get_products():
    if response.status_code == 200:
        products = response.json()
        quantity = int(input('¿Cuántos productos quieres ver?: '))
        print(products)
        for product in products[:quantity]:
            print(f"ID: {product['id']}, nombre: {product['title']}, precio: {product['price']}")
    else:
        print('No se pudo obtener la lista de productos')

# Cual es el precio promedio de los productos
def avg_price():
    if response.status_code == 200:
        products = response.json()
        prices = [product['price'] for product in products]
        avg = sum(prices) / len(prices)
        print(f"El precio promedio de los productos es: {avg}")
    else:
        print('No se pudo obtener la lista de productos')