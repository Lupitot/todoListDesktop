import sys
from PySide6 import QtWidgets, QtCore
from todoListe.window import Window


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    QtCore.QCoreApplication.setApplicationName("To Do List")

    widget = Window()
    widget.show()
    widget.resize(800, 600)

    sys.exit(app.exec())