import nfc

class nfcModule:

    def __init__(self):
        self.clf = nfc.ContactlessFrontend('tty:AMA2:pn532')
        target = None
        while target is None:
            target = self.clf.sense(nfc.clf.RemoteTarget('106A'), nfc.clf.RemoteTarget('106B'),
                                    nfc.clf.RemoteTarget('212F'))
            if target is None:
                pass
            else:
                tag = nfc.tag.activate(self.clf, target)
                print(str(tag).split("ID="))
                self.clf.close()
                return str(tag).split("ID=")[1]

