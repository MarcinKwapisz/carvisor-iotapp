import nfc

def get_tag():
    clf = nfc.ContactlessFrontend('tty:AMA2:pn532')
    target = None
    while target is None:
        target = clf.sense(nfc.clf.RemoteTarget('106A'), nfc.clf.RemoteTarget('106B'),
                                nfc.clf.RemoteTarget('212F'))
        if target is None:
            pass
        else:
            tag = nfc.tag.activate(clf, target)
            print(str(tag).split("ID="))
            clf.close()
            return str(tag).split("ID=")[1]

