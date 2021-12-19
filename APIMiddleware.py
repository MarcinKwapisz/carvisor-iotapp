from flask import Flask,request,jsonify, Response
from threading import Thread
import os
# from savingModule import Saver
import json
import requests

app = Flask(__name__)

@app.route('/<path:path>/API/track/updateTrackData/', methods=['POST'])
def send(path):
    if request.method == 'POST':
        data = request.data.decode("utf-8")
        Thread(target=send_obd, args=(path+"/API/track/updateTrackData/", data)).start()
        return jsonify('Sended')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET','POST'])
def index(path):
    if request.method == 'GET':
        try:
            request_to_API = sess.request("GET", "https://" + path)
            return jsonify(request_to_API.json()), request_to_API.status_code
        except requests.exceptions.RequestException:
            return failure_response.content, failure_response.status_code
        except json.decoder.JSONDecodeError:
            return request_to_API.status_code,
    if request.method == 'POST':
        data = request.data.decode("utf-8")
        p = requests.Request("POST", "https://" + path, data=data)
        ready_request = sess.prepare_request(p)
        try:
            req = sess.send(ready_request)
        except requests.exceptions.RequestException:
            return failure_response
        return Response("{'a':'b'}", status=req.status_code, mimetype='application/json')


def send_obd(path, data):
    p = requests.Request("POST", "https://" + path, data=data)
    ready_request = sess.prepare_request(p)
    try:
        print(data)
        req = sess.send(ready_request)
    except requests.exceptions.RequestException:
        print("except")
        return failure_response
    return Response("{'a':'b'}", status=req.status_code, mimetype='application/json')


def create_own_response():
    failure_response = requests.models.Response()
    failure_response.code = "expired"
    failure_response.error_type = "expired"
    failure_response.status_code = 400
    return failure_response

if __name__ == "__main__":
    sess = requests.Session()
    # savr = Saver()
    failure_response = create_own_response()
    app.run(host='0.0.0.0', port=5000, threaded=True)

