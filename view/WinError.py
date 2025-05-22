from . import *

class NetworkError(QMainWindow):
    def __init__(self):
        super().__init__()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.label)

        buttonLayout = QHBoxLayout()
        closeBtn = QPushButton("Закрыть")
        copyErr = QPushButton("Скопировать")

        buttonLayout.addWidget(closeBtn)
        buttonLayout.addWidget(copyErr)

        self.mainLayout.addLayout(buttonLayout)

        centralWidget.setLayout(self.mainLayout)

        closeBtn.clicked.connect(self._closeWin)
        copyErr.clicked.connect(self._copyError)

    def open(self, title="NetworkError", text="1001 - нет подключения к интернету!"):
        self.setWindowTitle(title)
        self.label.setText(f"Error: {text}")
        self.show()

    def _copyError(self):
        from PyQt6.QtWidgets import QApplication
        clipboard = QApplication.clipboard()
        clipboard.setText(self.label.text())

    def _closeWin(self):
        self.close()