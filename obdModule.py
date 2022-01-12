import obd
import time


class ObdReader:

    def __init__(self,send):
        # self.logging()
        # self.connection = obd.Async('/dev/pts/2',fast=False, delay_cmds=1)
        self.connection = obd.Async(fast=False, delay_cmds=1)
        self.commands_watching = [obd.commands.RPM,obd.commands.SPEED,obd.commands.THROTTLE_POS,obd.commands.GET_CURRENT_DTC, obd.commands.FUEL_LEVEL]
        self.sender = send


    def logging(self):
        # Function created when you want to see all data from obd logger
        obd.logger.setLevel(obd.logging.DEBUG)

    def check_connection(self):
        return self.connection.is_connected()


    def start_read(self):
        # connecting to OBD module and
        for i in self.commands_watching:
            self.connection.watch(i, callback=self.sender.pack)
        self.connection.start()

    def check_supported_commands(self):
        #checking which commands are supported by obd
        commands = self.connection.supported_commands
        for i in commands:
            print(i)
