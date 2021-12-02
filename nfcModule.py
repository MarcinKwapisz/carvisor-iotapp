import nfc
from nfc.clf import RemoteTarget


class nfcModule:

    def __init__(self):
        self.clf = nfc.ContactlessFrontend('tty:AMA2:pn532')


    def get_tag(self):
        target = None
        while target is None:
            target = self.clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))
            if target is None:
                pass
            else:
                tag = nfc.tag.activate(self.clf, target)
                return str(tag).split("ID=")[1]




