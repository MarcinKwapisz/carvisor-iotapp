from flask import Flask,request,jsonify
from threading import Thread
import os
import json
import requests

app = Flask(__name__)

@app.route('/<path:path>/API/track/updateTrackData/', methods=['POST'])
def send(path):
    if request.method == 'POST':
        data = request.json
        print(path+"/API/track/updateTrackData/")
        Thread(target=send_obd, args=(path+"/API/track/updateTrackData/",data)).start()
        return jsonify('Sended')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET','POST'])
def index(path):
    if request.method == 'GET':
        try:
            request_to_API = session.request("GET", "https://" + path)
            return jsonify(request_to_API.json()), request_to_API.status_code
        except requests.exceptions.RequestException:
            return failure_response.content, failure_response.status_code
        except json.decoder.JSONDecodeError:
            return request_to_API.content, request_to_API.status_code,
    if request.method == 'POST':
        p = requests.post("http://" + path, json=request.json)
        return p.json(), p.status_code


def send_obd(path, data):
    p = requests.post("http://" + path, json=data)
    if p.status_code != 200:
        pass
    else:
        self.send_to_db(pata,data)


def create_own_response():
    failure_response = requests.models.Response()
    failure_response.code = "expired"
    failure_response.error_type = "expired"
    failure_response.status_code = 400
    return failure_response

if __name__ == "__main__":
    session = requests.Session()
    failure_response = create_own_response()
    app.run(host='0.0.0.0', port=5000, threaded=True)

