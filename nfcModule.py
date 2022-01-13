import nfc
from time import sleep
from gpiozero import Buzzer
from time import sleep

def get_tag():
    buzzer = Buzzer(17)
    clf = nfc.ContactlessFrontend('tty:AMA2:pn532')
    target = None
    while target is None:
        buzzer.on()
        sleep(0.2)
        target = clf.sense(nfc.clf.RemoteTarget('106A'), nfc.clf.RemoteTarget('106B'),
                                nfc.clf.RemoteTarget('212F'))
        buzzer.off()
        if target is None:
            pass
        else:
            tag = nfc.tag.activate(clf, target)
            clf.close()
            return str(tag).split("ID=")[1]

