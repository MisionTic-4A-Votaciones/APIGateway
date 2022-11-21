from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

report_blueprints = Blueprint("report_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-voting') + "/report"


@report_blueprints.route("/reports", methods=['GET'])
def get_all_reports() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@report_blueprints.route("/report/<string:id_>", methods=['GET'])
def get_report_by_id(id_: str) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@report_blueprints.route("/report/insert", methods=['POST'])
def insert_report() -> dict:
    report = request.get_json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS, json=report)
    return response.json()


@report_blueprints.route("/report/update/<string:id_>", methods=['PUT'])
def update_report(id_: str) -> dict:
    report = request.get_json()
    url = url_base + f'/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=report)
    return response.json()


@report_blueprints.route("/report/delete/<string:id_>", methods=['DELETE'])
def delete_report(id_: str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()

