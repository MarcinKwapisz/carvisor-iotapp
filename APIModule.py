import datetime
import logging
import requests
import json
from gpiozero import Button
class RequestAPI:

    def __init__(self, login_data,gps):
        # initialize variables with login data from config file
        self.gps = gps
        self.base_url = "http://home.marcinkwapisz.pl:5000/"+login_data['address']
        self.connection_retries_number = 3
        self.login_data = json.dumps({"licensePlate": login_data['licenseplate'], 'password': login_data['password']})
        self.create_own_response()
        self.session = requests.Session()
        self.send_path(login_data['address'])
        self.start_session_car()

    def POST(self,url,data_to_send={}):
        req = requests.Request("POST", self.base_url + url, data=data_to_send)
        ready_request = self.session.prepare_request(req)
        try:
            request =  self.session.send(ready_request)
        except requests.exceptions.RequestException:
            return self.failure_response
        return request

    def GET(self,url):
        try:
            request = self.session.request("GET", self.base_url + url)
        except requests.exceptions.RequestException:
            return self.failure_response
        return request

    def send_path(self, address):
        self.POST("setting/path", json.dumps(address))
        pass


    def start_session_car(self):
        # starting new session with server
        for i in range(self.connection_retries_number):
            response = self.POST("API/carAuthorization/authorize",self.login_data)
            if response.status_code == 200:
                logging.debug("Device connected to server")
                break
            elif response.status_code == 406:
                logging.warning("Wrong licence plate or/and password in config file")
                break
            else:
                logging.warning("Server unreachable, error code: " + str(response.status_code))


    def send_obd_data(self, obd_data):
        response = self.POST("API/track/updateTrackData/",json.dumps(obd_data))
        if response.status_code == 200:
            logging.debug("Sending obd data finished")
        else:
            logging.warning("Problem occurred when sending obd data to server, error code: " + str(response.status_code))

    def start_track(self,tag):
        gps_pos = self.gps.get_only_position_values()
        start_data = json.dumps({ "nfc_tag":tag, "time": datetime.datetime.now().strftime("%s"), "private": Button(2).is_active, "gps_longitude":gps_pos[0],"gps_latitude":gps_pos[1]})
        for i in range(self.connection_retries_number):
            response = self.POST("API/track/start",start_data)
            if response.status_code == 200:
                logging.debug("Track started")
                break
            elif response.status_code == 409:
                logging.debug("Track exist, working on existing track")
                break
            else:
                logging.warning("Problem occurred while starting a new track: " + str(response.status_code))


    def check_authorization(self):
        response = self.GET("API/carAuthorization/status")
        if response.status_code == 200:
            logging.debug("Track started")
            return response.json()["logged"]
        elif response.status_code == 409:
            logging.debug("Track exist, working on existing track")
            return False
        else:
            logging.warning("Problem occurred while starting a new track: " + str(response.status_code))
            return False

    def get_config_from_server(self):
        response = self.GET("API/carConfiguration/get/")
        if response.status_code == 200:
            logging.debug("Config from server downloaded")
            return response.json()
        else:
            logging.warning("Problem occurred with getting a configuration: " + str(response.status_code))
            return False


    def create_own_response(self):
        self.failure_response = requests.models.Response()
        self.failure_response.code = "expired"
        self.failure_response.error_type = "expired"
        self.failure_response.status_code = 400
