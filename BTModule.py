import logging
import bluetooth
import os
import subprocess

class Bluetooth:

    def __init__(self):
        os.system("./BTStart.sh")
        BT_name_output = subprocess.check_output("sudo hciconfig hci0 name | grep Name | cut -d' ' -f2", shell=True).decode("UTF-8").rstrip("\n").replace("'","")
        print(BT_name_output)
        self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.server_sock.bind(("", bluetooth.PORT_ANY))
        self.server_sock.listen(1)

        self.port = self.server_sock.getsockname()[1]

        uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

        bluetooth.advertise_service(self.server_sock, BT_name_output, service_id=uuid,
                                    service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                                    profiles=[bluetooth.SERIAL_PORT_PROFILE]
                                    )

    def connect(self):
        print("gg")
        logging.debug("Waiting for bluetooth connection on RFCOMM channel", self.port)

        client_sock, client_info = self.server_sock.accept()
        logging.debug("Accepted bluetooth connection from", client_info)
        while True:
            try:
                data = client_sock.recv(1024)
            except bluetooth.btcommon.BluetoothError:
                break

        logging.debug("Bluetooth disconnected.")

        client_sock.close()
        self.server_sock.close()
        logging.debug("BT all done.")
        return data.decode("UTF-8")
