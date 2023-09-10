import requests

# URL de la API de JSONPlaceholder para obtener datos de usuarios
url = 'https://jsonplaceholder.typicode.com/users'

# Realizar una solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener los datos en formato JSON
    datos_usuarios = response.json()

    # Imprimir información de los usuarios
    for usuario in datos_usuarios:
        print(f"ID: {usuario['id']}")
        print(f"Nombre: {usuario['name']}")
        print(f"Email: {usuario['email']}")
        print("----")
else:
    print('La solicitud no fue exitosa. Código de estado:', response.status_code)