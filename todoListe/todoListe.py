import json
from PySide6 import QtCore, QtWidgets


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.listeAdd = []
        self.currentItem = None
        
        with open('todoListe/dataToDo.json', 'r') as f:
            data = f.read()
        if data:
            self.listeAdd = json.loads(data)
        else:
            self.listeAdd = []

        self.layout = QtWidgets.QVBoxLayout(self)
        self.buttonAdd = QtWidgets.QPushButton("Add")
        self.inputText = QtWidgets.QLineEdit()
        self.listWidget = QtWidgets.QListWidget()
        self.buttonDelete = QtWidgets.QPushButton("Terminer")
        
        

        for item in self.listeAdd:
            self.listWidget.addItem(item)
            
        self.layout.addWidget(self.inputText)
        self.layout.addWidget(self.buttonAdd)
        self.layout.addWidget(self.listWidget)
        self.layout.addWidget(self.buttonDelete)   


        self.listWidget.itemClicked.connect(self.setItemCurrent)
        self.buttonDelete.clicked.connect(self.deleteItemCurrent)
        self.buttonAdd.clicked.connect(self.add)
        
    

    @QtCore.Slot()
    def setItemCurrent(self, item):
        self.currentItem = item
    
    
    def add(self):
        if(self.inputText.text() == ""):
            return
        
        self.listeAdd.append(self.inputText.text())
        self.listWidget.addItem(self.inputText.text())
        print(self.listeAdd)
        self.inputText.setText("")
        
        with open('dataToDo.json', 'w') as f:
            json.dump(self.listeAdd, f)

    def deleteItemCurrent(self):
        current_item = self.currentItem
        print(current_item)
        if current_item is not None:
            self.listeAdd.remove(current_item.text())
            self.listWidget.takeItem(self.listWidget.currentRow()) 
            with open('dataToDo.json', 'w') as f:
                json.dump(self.listeAdd, f)
