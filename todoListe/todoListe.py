import json
from PySide6 import QtCore, QtWidgets
from todoListe.todoListeFinished import WidgetFinishedTask


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.listeAdd = []
        self.currentItem = None
        self.ListSelectedItem = None
        self.widgetFinished = WidgetFinishedTask()


        with open('./dataToDo.json', 'r') as f:
            data = f.read()
        if data:
            self.listeAdd = json.loads(data)
        else:
            self.listeAdd = []


        layoutMain = QtWidgets.QVBoxLayout()
        layoutList = QtWidgets.QHBoxLayout()
        layoutText = QtWidgets.QHBoxLayout()
        layoutButton = QtWidgets.QHBoxLayout()


        self.buttonAdd = QtWidgets.QPushButton("Add")
        self.buttonAdd.setStyleSheet(
            "background-color  : #3AA183;"
            "color : #FFFFFF;"
            "font-size : 20px;"
        )
        self.inputText = QtWidgets.QLineEdit()
        self.inputText.setStyleSheet(
            """
            QLineEdit {
                background-color : #FFFFFF;
                border : 3px solid #C2C1C1;
                font-size : 20px;
            }
            QLineEdit::item:selected {
                background-color: #3AA183;
                color: #FFFFFF;
            }
            """
        )
        self.inputText.setPlaceholderText("Enter a task")
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setStyleSheet(
            """
                QListWidget {
                    background-color : #FFFFFF;
                    border : 6px solid #C2C1C1;
                    font-size : 20px;
                }
                QListWidget::item:selected {
                    background-color: #3AA183;
                    border: none;
                    color: #FFFFFF;
                }
            """
        )
        self.listWidget.setSpacing(5)

        self.buttonFinished = QtWidgets.QPushButton("Finished")
        self.buttonFinished.setStyleSheet(
            "background-color  : #3AA183;"
            "color : #FFFFFF;"
            "font-size : 20px;"
        )
        self.buttonDelete = QtWidgets.QPushButton("Delete")
        self.buttonDelete.setStyleSheet(
            "background-color  : #D63E3E;"
            "color : #FFFFFF;"
            "font-size : 20px;"
        )
        self.textTodo = QtWidgets.QLabel("To do")
        self.textTodo.setStyleSheet(
            "font-size : 20px;" 
            "background-color : #C2C1C1;"
        )
        self.textTodo.setAlignment(QtCore.Qt.AlignCenter) 
        self.textFinished = QtWidgets.QLabel("Finished")
        self.textFinished.setStyleSheet(
            "font-size : 20px;" 
            "background-color : #C2C1C1;"
        )
        self.textFinished.setAlignment(QtCore.Qt.AlignCenter)
        
        

        for item in self.listeAdd:
            self.listWidget.addItem(item)
            

        layoutList.addWidget(self.listWidget)
        layoutList.addWidget(self.widgetFinished.listWidgetFinished)


        layoutText.addWidget(self.textTodo)
        layoutText.addWidget(self.textFinished)

        layoutButton.addWidget(self.buttonFinished)
        layoutButton.addWidget(self.buttonDelete)   



        layoutMain.addWidget(self.inputText)
        layoutMain.addWidget(self.buttonAdd)
        layoutMain.addLayout(layoutText)
        layoutMain.addLayout(layoutList)
        layoutMain.addLayout(layoutButton)




        self.setLayout(layoutMain)


        self.widgetFinished.listWidgetFinished.itemClicked.connect(self.taskFinished)
        self.listWidget.itemClicked.connect(self.setItemCurrent)
        self.buttonDelete.clicked.connect(self.deleteItemCurrent)
        self.buttonAdd.clicked.connect(self.add)
        self.buttonFinished.clicked.connect(self.finishedTask)
        


    @QtCore.Slot()

    def finishedTask(self):
        self.widgetFinished.finishedTask(self.currentItem)
        
        current_item = self.currentItem
        self.listeAdd.remove(current_item.text())
        self.listWidget.takeItem(self.listWidget.currentRow()) 
        with open('./dataToDo.json', 'w') as f:
            json.dump(self.listeAdd, f)
        

    def taskFinished(self, item):
        self.ListSelectedItem = "Finished"
        self.currentItem = item

    def setItemCurrent(self, item):
        self.ListSelectedItem = None
        self.currentItem = item
    
    def add(self):
        if(self.inputText.text() == ""):
            return
        
        self.listeAdd.append(self.inputText.text())
        self.listWidget.addItem(self.inputText.text())
        print(self.listeAdd)
        self.inputText.setText("")
        
        with open('./dataToDo.json', 'w') as f:
            json.dump(self.listeAdd, f)

    def deleteItemCurrent(self):
        print("valeur de ListSelectedItem", self.ListSelectedItem)
        current_item = self.currentItem
        print(current_item)
        if current_item is not None:
            if self.ListSelectedItem == "Finished":
                self.widgetFinished.listeAddFinished.remove(current_item.text())
                self.widgetFinished.listWidgetFinished.takeItem(self.widgetFinished.listWidgetFinished.currentRow()) 
                with open('./dataTerminate.json', 'w') as f:
                    json.dump(self.widgetFinished.listeAddFinished, f)
            else:
                self.listeAdd.remove(current_item.text())
                self.listWidget.takeItem(self.listWidget.currentRow()) 
                with open('./dataToDo.json', 'w') as f:
                    json.dump(self.listeAdd, f)
        else:
            print("No item selected")
        self.currentItem = None
