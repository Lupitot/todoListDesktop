from todoListe.todoListe import MainWidget
from PySide6.QtGui import QIcon
from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.widget1 = MainWidget()

        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.widget1)

        self.setLayout(layout)
        self.setWindowIcon(QIcon('./fish-bowl.png'))