import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        # self.button = QtWidgets.QPushButton("Click me!")
        # self.text = QtWidgets.QLabel("Hello World",
        #                              alignment=QtCore.Qt.AlignCenter)
        self.listeAdd = []
        

        
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.buttonAdd = QtWidgets.QPushButton("Add")
        self.inputText = QtWidgets.QLineEdit()
        self.listWidget = QtWidgets.QListWidget()
        
        
        self.layout.addWidget(self.inputText)
        self.layout.addWidget(self.buttonAdd)
        self.layout.addWidget(self.listWidget)
        
        self.listWidget.itemDoubleClicked.connect(self.deleteItemCurrent)
        
        self.buttonAdd.clicked.connect(self.add)

        
        
        
        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)

        # self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    # def magic(self):
    #     self.text.setText(random.choice(self.hello))
    def add(self):
        self.listeAdd.append(self.inputText.text())
        self.listWidget.addItem(self.inputText.text())
        print(self.listeAdd)
        self.inputText.setText("")
    def deleteItemCurrent(self):
        
        





class NewWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.nombre = 0
        self.button = QtWidgets.QPushButton("random nombre")
        self.number = QtWidgets.QLabel("0",
                                        alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.number)
        self.number.setFont(QtGui.QFont("Comic Sans MS", 20))

        
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.nombre = random.randint(0, 100)
        self.number.setText(str(self.nombre))
        if  self.nombre == 84 or self.nombre == 66 :
            print(self.nombre)
            self.number.setStyleSheet("color: green")
        else:
            self.number.setStyleSheet("color: fuchsia")


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.widget1 = MyWidget()
        # self.widget2 = NewWidget()
        
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.widget1)
        # layout.addWidget(self.widget2)
        
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Window()
    widget.show()
    widget.resize(800, 600)

    sys.exit(app.exec())















