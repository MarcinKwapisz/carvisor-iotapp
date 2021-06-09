import re

class gps:

        def __init__(self):
                self.longitude = 16.92397
                self.latitude = 52.45726

        def get_current_position_from_phone(self):
                try:
                        location_file = open("location", 'r').readlines()[-3]
                        location_file = location_file.split("│")[1]
                        self.longitude, self.latitude = re.findall('[0-9]*[\.]{1}[0-9]*', location_file)
                except UnicodeDecodeError:
                        print("ERRROROROROROORORRO")
                return {'longitude': float("%.5f" % float(self.longitude)),
                                        "latitude": float("%.5f" % float(self.latitude))}

        def get_fake_gps_position(self):
                position = {'longitude': float("%.5f" % self.longitude),
                 "latitude": float("%.5f" % self.latitude)}
                return position

        def get_only_position_values(self):
                self.fake_location_move()
                self.longitude = float("%.5f" % float(self.longitude))
                self.latitude = float("%.5f" % float(self.latitude))
                return [self.longitude,self.latitude]

        def fake_location_move(self):
                self.longitude -= 0.00010

        def get_position(self):
                self.fake_location_move()
                # return self.get_current_position_from_phone()
                return self.get_fake_gps_position()
