import requests

security_backend = "http://127.0.0.1:8080"
headers = {"Content-Type": "application/json; charset=utf-8"}

# Create roles
roles = [
    {"name": "Administrador", "description": "Administrador del sistema de registro de votos"},
    {"name": "Jurado", "description": "Encargado de ingresar la información de la votación en el sistema"},
    {"name": "Ciudadano", "description": "Persona natural"}
]

url = f'{security_backend}/rol/insert'
admin = None
for rol in roles:
    response = requests.post(url, headers=headers, json=rol)
    if rol.get("name") == "Administrador":
        admin = response.json()
    print(response.json())
print('=' * 30)

# Add permissions

modules = ["candidate", "party", "table", "result", "user", "rol"]
endpoints = [("s", "GET"), ("/?", "GET"), ("/insert", "POST"), ("/update/?", "PUT"), ("/delete/?", "DELETE")]
url = f'{security_backend}/permission/insert'
for module in modules:
    for endpoint, method in endpoints:
        permission = f'/{module}{endpoint}'
        body = {
            "url": permission,
            "method": method
        }
        response = requests.post(url, headers=headers, json=body)
        print(response.json())
        data_ = response.json()
        url_relation = f'{security_backend}/rol/update/{admin.get("idRol")}/add_permission/{data_.get("id")}'
        response = requests.put(url_relation, headers=headers)
