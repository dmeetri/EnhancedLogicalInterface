import socket

from view.Settings import *
from view.WinError import *

def onEnable():
    app = QApplication([])

    if not is_connected():
        netErr = NetworkError()
        netErr.open()
    else:
        setWin = SettingWinMini()
        setWin.btnOpenSettings()
        setWin.show()

    app.exec()

def is_connected():
    REMOTE_SERVER = "one.one.one.one"

    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        s.close()

        return True
    except Exception:
        pass
    return False

def onDisable():
    pass

if __name__ == "__main__":
    onEnable()