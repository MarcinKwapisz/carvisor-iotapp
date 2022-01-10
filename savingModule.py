from tinydb import TinyDB
import json
import datetime
import time
class Saver:

    def __init__(self, stamp):
        if stamp == 'queue':
            open(stamp+".json", 'w').close()
        self.db = TinyDB(str(stamp)+'.json')
        self.amount_of_data = len(self.db)
        self.address = self.check_config_file()


    def check_config_file(self):
        while os.path.realpath(__file__))+"/config.ini" is False:
            time.sleep(5)


    def insert(self, base, data, counter=0):
        if counter >= 3:
            return False
        try:
            self.db.insert(data)
            return True
        except AssertionError:
            return self.insert(base, data, counter + 1)

    def send_obd_data(self, obd_data):
        obd_data = json.loads(obd_data)
        for i in obd_data:
            print(obd_data[i])
            self.insert(self.db, obd_data)

    def get_all_data(self):
        return self.db.table('_default').all()

    def get_amount_of_data(self):
        self.amount_of_data = len(self.db)
        return self.amount_of_data

    def get_path(self, path):
        print(data)
        self.path = path

    def send_payload(self,):
        while self.get_amount_of_data() > 0:
            table = self.db.table('_default')
            entry = table.all()[0]
            table.remove(doc_ids=[entry.doc_id])
            response = self.API.send_saved_data(dict(entry))
            if response:
                self.insert(self.db, entry)
            else:
                pass

    def get_API(self,API):
        self.API = API

    def remove_entry(self,doc_id):
        table = self.db.table('_default')
        table.remove(doc_ids=[doc_id])
