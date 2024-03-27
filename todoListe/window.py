from todoListe.todoListe import MainWidget
# from todoListe.todoListeTerminate import WidgetTerminateTask
from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.widget1 = MainWidget()

        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.widget1)

        self.setLayout(layout)