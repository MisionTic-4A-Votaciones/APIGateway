from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

user_blueprints = Blueprint("user_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-security') + "/user"


@user_blueprints.route("/users", methods=['GET'])
def get_all_users() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@user_blueprints.route("/user/<string:id_>", methods=['GET'])
def get_user_by_id(id_: int) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@user_blueprints.route("/insert", methods=['POST'])
def insert_user() -> dict:
    user = requests.get().json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS, json=user)
    return response.json()


@user_blueprints.route("/update/<string:id_>", methods=['PUT'])
def update_user(id_: int) -> dict:
    user = requests.get().json()
    url = url_base + f'/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=user)
    return response.json()


@user_blueprints.route("/delete/<string:id_>", methods=['DELETE'])
def delete_user(id_: int) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()

