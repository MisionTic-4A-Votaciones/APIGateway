from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

candidate_blueprints = Blueprint("candidate_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-voting') + "/candidate"


@candidate_blueprints.route("/candidates", methods=['GET'])
def get_all_candidates() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@candidate_blueprints.route("/candidate/<string: id_>", methods=['GET'])
def get_candidate_by_id(id_: str) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@candidate_blueprints.route("/insert", methods =['POST'])
def insert_candidate() -> dict:
    candidate = requests.get().json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS, json=candidate)
    return response.json()


@candidate_blueprints.route("/update/<string:id_>", methods=['PUT'])
def update_candidate(id_: str) -> dict:
    candidate = requests.get().json()
    url = url_base + f'/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=candidate)
    return response.json()


@candidate_blueprints.route("/delete/<string:id_>", methods =['DELETE'])
def delete_candidate(id_: str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()

