import logging

import bluetooth

class Bluetooth:

    def __init__(self):
        self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.server_sock.bind(("", bluetooth.PORT_ANY))
        self.server_sock.listen(1)

        self.port = self.server_sock.getsockname()[1]

        uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

        bluetooth.advertise_service(self.server_sock, "CarVisor", service_id=uuid,
                                    service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                                    profiles=[bluetooth.SERIAL_PORT_PROFILE],
                                    # protocols=[bluetooth.OBEX_UUID]
                                    )

    def connect(self):
        logging.debug("Waiting for connection on RFCOMM channel", self.port)

        client_sock, client_info = self.server_sock.accept()
        logging.debug("Accepted connection from", client_info)
        data = ''
        while True:
            data += client_sock.recv(1024)
            print("Received", data)
            client_sock.send("ok")


        logging.debug("Disconnected.")

        client_sock.close()
        self.server_sock.close()
        logging.debug("All done.")

bt = Bluetooth()
bt.connect()