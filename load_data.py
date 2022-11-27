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
jury = None
for rol in roles:
    response = requests.post(url, headers=headers, json=rol)
    if rol.get("name") == "Administrador":
        admin = response.json()
    if rol.get("name") == "Jurado":
        jury = response.json()
    if rol.get("name") == "Ciudadano":
        citizen = response.json()
    print(response.json())

# Add permissions for Administrator

modules = ["candidate", "party", "table", "result", "user", "rol", "report"]
endpoints = [("s", "GET"), ("/?", "GET"), ("/insert", "POST"), ("/update/?", "PUT"), ("/delete/?", "DELETE"),
             ("/get_greatest_vote", "GET"), ("/get_results_by_candidate", "GET")]
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

        # To add permissions to Jury

modules = ["result", "report"]
endpoints = [("s", "GET"), ("/?", "GET"), ("/insert", "POST"), ("/update/?", "PUT"), ("get_greatest_vote", "GET"),
             ("/get_results_by_candidate", "GET")]

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
        url_relation = f'{security_backend}/rol/update/{jury.get("idRol")}/add_permission/{data_.get("id")}'
        response = requests.put(url_relation, headers=headers)

# To allow access to citizens only to the report module
modules = ["report"]
endpoints = [("/get_greatest_vote", "GET"), ("/get_results_by_candidate", "GET")]

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
        url_relation = f'{security_backend}/rol/update/{citizen.get("idRol")}/add_permission/{data_.get("id")}'
        response = requests.put(url_relation, headers=headers)
