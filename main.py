from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import (JWTManager)

from waitress import serve

from datetime import timedelta
import json
import requests
import re


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "voteG10"
cors = CORS(app)
jwt = JWTManager(app)


@app.route("/", methods=['GET'])
def home():
    response = {"message": "Welcome to the voting API Gateway..."}
    return response


# Config and execute app
def load_file_config():
    """

    :return:
    """
    with open("config.json", 'r') as file_:
        data = json.load(file_)
    return data


if __name__ == "__main__":
    data_config = load_file_config()
    print("API Gateway Server Running: http://" + data_config.get("url-backend") + ":" + str(data_config.get("port")))
    serve(app, host=data_config.get("url-backend"), port=data_config.get("port"))
