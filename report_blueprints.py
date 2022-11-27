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


@report_blueprints.route("/report/get_greatest_vote", methods=['GET'])
def get_greatest_vote(id_: str) -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@report_blueprints.route("/report/get_results_by_candidate", methods=['GET'])
def get_results_by_candidate() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


