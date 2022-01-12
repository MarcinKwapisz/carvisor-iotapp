from serial import Serial
import pynmea2


class gps:

    def __init__(self):
        self.longitude = None
        self.latitude = None
        self.serial = Serial("/dev/ttyAMA4", baudrate=9600, timeout=0.2)

    def gps(self):
        while True:
            try:
                gps_serial_line = self.serial.readline().decode("UTF-8")
            except UnicodeDecodeError:
                gps_serial_line = self.serial.readline()
            if gps_serial_line[0:6] == '$GPRMC':
                gps_output = pynmea2.parse(gps_serial_line)
                if float("%.5f" % float(gps_output.longitude)) == 0.0:
                    pass
                elif float("%.5f" % float(gps_output.longitude)) == 0.0:
                    self.latitude = float("%.5f" % float(gps_output.latitude))
                    self.longitude = float("%.5f" % float(gps_output.longitude))
                if self.longitude == None:
                    pass
                else:
                    return

    def get_only_position_values(self):
        self.gps()
        return [self.longitude, self.latitude]

    def get_position(self):
        self.gps()
        return {"longitude": self.longitude, "latitude": self.latitude}
