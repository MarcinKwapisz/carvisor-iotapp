import nfc
from time import sleep
from gpiozero import TonalBuzzer
from time import sleep

def get_tag():
    buzzer = TonalBuzzer(17)
    buzzer.play(220)
    clf = nfc.ContactlessFrontend('tty:AMA2:pn532')
    target = None
    while target is None:
        target = clf.sense(nfc.clf.RemoteTarget('106A'), nfc.clf.RemoteTarget('106B'),
                                nfc.clf.RemoteTarget('212F'))
        if target is None:
            pass
        else:
            buzzer.stop()
            tag = nfc.tag.activate(clf, target)
            clf.close()
            return str(tag).split("ID=")[1]

