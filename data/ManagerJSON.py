import json
from typing import List, Any
import os

class JsonManage:
    def __init__(self):
        self.fileName = "config.json"
        self.file = {
            "DISPLAY_MINI_WIN_SETING": True,
            "DISPLAY_CORNER": "BottomRight",
        }

    def init(self):
        if not os.path.exists(self.fileName):
            self._createFile(self.fileName, self.file)

    def _createFile(self, fileName, file):
        with open(fileName, "w", encoding="utf-8") as f:
            json.dump(file, f, ensure_ascii=False, indent=4)

    def updateFile(self, fileName: str, fileKey: str, fileValue):
        data = self.getFile(fileName)
        data[fileKey] = fileValue

        with open("config.json", "w", encoding="utf-8") as f:
            self._createFile(fileName, data)

    def getFile(self, fileName) -> List[any]:
        with open(fileName, "r", encoding="utf-8") as f:
            return json.load(f)