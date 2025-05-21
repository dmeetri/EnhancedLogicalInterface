from PyQt6.QtWidgets import QApplication
from view.settings import *

def onEnable():
    app = QApplication([])

    setWin = SettingWinMini()
    setWin.show()

    app.exec()

def onDisable():
    pass

if __name__ == "__main__":
    onEnable()