from flask import Flask,request,jsonify, Response
from threading import Thread
from savingModule import Saver
import json
import requests

app = Flask(__name__)

@app.route('/<path:path>/API/track/updateTrackData/', methods=['POST'])
def send(path):
    if request.method == 'POST':
        data = request.data.decode("utf-8")
        Thread(target=send_obd, args=(path+"/API/track/updateTrackData/", data)).start()
        return jsonify('Sended')

@app.route('/setting/path', methods=['POST'])
def send_path(path):
    if request.method == 'POST':
        data = request.data.decode("utf-8")
        que.get_path(data)


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
        req = sess.send(ready_request)
    except requests.exceptions.RequestException:
        return failure_response
    if req.status_code != 200:
        que.send_obd_data(data)
    else:
        que.get_amount_of_data()
    return Response("{'a':'b'}", status=req.status_code, mimetype='application/json')

def send_obd_saved(path, data):
    p = requests.Request("POST", "https://" + path, data=data)
    ready_request = sess.prepare_request(p)
    try:
        req = sess.send(ready_request)
    except requests.exceptions.RequestException:
        return failure_response
    if req.status_code != 200:
        return True
    else:
        return False


def create_own_response():
    failure_response = requests.models.Response()
    failure_response.code = "expired"
    failure_response.error_type = "expired"
    failure_response.status_code = 400
    return failure_response

if __name__ == "__main__":
    save = 1
    sess = requests.Session()
    que = Saver("queue")
    failure_response = create_own_response()
    app.run(host='0.0.0.0', port=5000, threaded=True)

