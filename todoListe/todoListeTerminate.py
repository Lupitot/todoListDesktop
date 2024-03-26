import json
from PySide6 import QtCore, QtWidgets


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.currentItem = None
        self.listeAddTerminate = []
        