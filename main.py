import logging
import time

from configModule import Config
from obdModule import ObdReader
from sendModule import Sender
from APIModule import RequestAPI
from gpsModule import gps
from BTModule import Bluetooth
import nfcModule
from gpiozero import Buzzer
from time import sleep


class CarVisor:

    def __init__(self):
        self.buzzer = Buzzer(17)
        self.start_logging()
        self.gps = gps(self.buzzer)
        self.BT = Bluetooth()
        self.config = Config('config.ini', self.BT)
        if self.config.check_server_credentials():
            self.API = RequestAPI(self.config.section_returner('login'), self.gps)
            if self.API.check_authorization():
                # everything is fine, IoT can send data to server
                self.get_config_from_server()
                # self.API.start_track("AAC")
                self.API.start_track(nfcModule.get_tag(self.buzzer))
            else:
                pass
        else:
            pass
        self.send = Sender(self.config.return_send_interval(), self.API, self.gps)
        self.init_obd()

    def start_logging(self):
        logging.basicConfig(filename='carvisor.log',
                            format='%(asctime)s %(levelname)-6s %(message)s',
                            level=logging.DEBUG,
                            datefmt='%Y-%m-%d %H:%M:%S')

    def init_obd(self):
        self.obd = ObdReader(self.send)
        while not self.obd.check_connection():
            time.sleep(5)
            self.obd = ObdReader(self.send)
        self.start_obd_reading()

    def start_obd_reading(self):
        self.obd.start_read()
        print("Rozpoczęto odczyt OBD.\n")
        while 1:
            time.sleep(60)

    def get_config_from_server(self):
        config = self.API.get_config_from_server()
        if config:
            self.config.get_config_from_server(config)
        else:
            pass


start = CarVisor()



