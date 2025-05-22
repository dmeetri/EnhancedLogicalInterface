from . import *

class SettingWinMini(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("set")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(100, 100)
        self.setPosition("BottomRight")

        self.SettigsOppen = None

        settingsOpenButton = QPushButton("Настройки", self)
        settingsOpenButton.resize(100, 100)
        settingsOpenButton.clicked.connect(self.btnOpenSettings)

    def setPosition(self, pointPosition = "TopLeft"):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        window_width = self.width()
        window_height = self.height()

        if pointPosition == "TopLeft":
            x, y = 0, 0
        elif pointPosition == "TopRight":
            x, y = screen_width - window_width, 0
        elif pointPosition == "BottomLeft":
            x, y = 0, screen_height - window_height
        elif pointPosition == "BottomRight":
            x, y = screen_width - window_width, screen_height - window_height
        elif pointPosition == "Center":
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
        else:
            x, y = 0, 0

        self.move(x, y)
    
    def btnOpenSettings(self):
        if self.SettigsOppen is None:
            self.SettigsOppen = PrimarySettingWin()
        self.SettigsOppen.show()
    

class PrimarySettingWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eli setting")
        self.setMinimumSize(QSize(600, 450))