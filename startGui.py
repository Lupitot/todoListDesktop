import sys
from PySide6 import QtWidgets
from todoListe.window import Window


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Window()
    widget.show()
    widget.resize(800, 600)

    sys.exit(app.exec())