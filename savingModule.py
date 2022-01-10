from tinydb import TinyDB
import json
import datetime
class Saver:

    def __init__(self, stamp):
        if stamp == 'queue':
            open(stamp, 'w').close()
        self.db = TinyDB(str(stamp)+'.json')
        self.amount_of_data = len(self.db)

    def send_obd_data(self, obd_data):
        obd_data = json.loads(obd_data)
        for i in obd_data:
            print(obd_data[i])
            self.db.insert(obd_data)

    def get_all_data(self):
        return self.db.table('_default').all()

    def get_amount_of_data(self):
        self.amount_of_data = len(self.db)
        return self.amount_of_data

    def get_path(self, path):
        self.path = path

    def send_payload(self):
        while self.get_amount_of_data() > 0:
            table = self.db.table('_default')
            entry = table.all()[0]
            table.remove(doc_ids=[entry.doc_id])
            response = self.API.send_saved_data(dict(entry))
            if response:
                pass
            else:
                self.send_obd_data(entry)

    def get_API(self,API):
        self.API = API

    def remove_entry(self,doc_id):
        table = self.db.table('_default')
        table.remove(doc_ids=[doc_id])
