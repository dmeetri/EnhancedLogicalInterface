from . import *
from data.ManagerJSON import JsonManage

jm = JsonManage()

class SettingWinMini(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("set")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(100, 100)
        self.setPosition()

        self.SettigsOppen = None

        settingsOpenButton = QPushButton("Настройки", self)
        settingsOpenButton.resize(100, 100)
        settingsOpenButton.clicked.connect(self.btnOpenSettings)

    def setPosition(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        window_width = self.width()
        window_height = self.height()
        
        data = jm.getFile("config.json")
        pointPosition = data.get("DISPLAY_CORNER")

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
        else:
            self.SettigsOppen.close()
            self.SettigsOppen = None
    

class ScrollWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

    def addWidget(self, widget):
        self.layout.addWidget(widget)

    def addLayout(self, layout):
        self.layout.addLayout(layout)


class CenteredContainer(QWidget):
    def __init__(self):
        super().__init__()

        self.container = QWidget()
        self.container.setFixedWidth(900)  # 👈 задаём ширину
        container_layout = QVBoxLayout()
        container_layout.setSpacing(0)
        container_layout.setContentsMargins(0, 0, 0, 0)
        self.container.setLayout(container_layout)

        outer_layout = QHBoxLayout()
        outer_layout.addStretch()
        outer_layout.addWidget(self.container)
        outer_layout.addStretch()

        self.setLayout(outer_layout)

    def addWidget(self, widget):
        self.container.layout().addWidget(widget)

    def addLayout(self, layout):
        self.container.layout().addLayout(layout)


class PrimarySettingWin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eli setting")
        self.setMinimumSize(QSize(1000, 500))

        self.container = QWidget()
        self.container.setFixedWidth(700)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        self.content = CenteredContainer()
        scroll.setWidget(self.content)

        self._setLabel("Настройки Eli", 35)

        #settings for displaying a mini settings window
        self._setLabel("Положение мини окна:", 25)

        settingButtonGrid = QGridLayout()
        
        labelSettingButton = ["Слева сверху", "Справа сверху", "Слева снизу", "Справа снизу"]
        posSettingButton = [(0,0), (0,1), (1,0), (1,1)]

        for pos, text in zip(posSettingButton, labelSettingButton):
            btn = QPushButton(text)
            btn.setStyleSheet("padding: 20px; margin: 2px;")
            btn.clicked.connect(self._setPosition)
            settingButtonGrid.addWidget(btn, pos[0], pos[1])

        self.content.addLayout(settingButtonGrid)

        self.setCentralWidget(scroll)

    def _setLabel(self, text: str, fontSize: int):
        label = QLabel(text)
        label.setMargin(5)
        label.setStyleSheet(f'font-size: {fontSize}px')
        self.content.addWidget(label)

    def _setPosition(self):
        sender = self.sender()
        smw = SettingWinMini()
        targetCorner = None

        print(sender)
        print()
        print(sender.text())

        if sender.text() == "Слева сверху":
            targetCorner = "TopLeft"
        elif sender.text() == "Справа сверху":
            targetCorner = "TopRight"
        elif sender.text() == "Слева снизу":
            targetCorner = "BottomLeft"
        elif sender.text() == "Справа снизу":
            targetCorner = "BottomRight"

        jm.updateFile("config.json", "DISPLAY_CORNER", targetCorner)
        smw.setPosition()