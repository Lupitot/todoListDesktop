import json
from PySide6 import QtCore, QtWidgets
from todoListe.todoListeTerminate import WidgetTerminateTask


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.listeAdd = []
        self.currentItem = None
        self.ListSelectedItem = None
        self.widgetTerminate = WidgetTerminateTask()


        with open('dataToDo.json', 'r') as f:
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

        self.buttonTerminate = QtWidgets.QPushButton("Terminate")
        self.buttonTerminate.setStyleSheet(
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
        self.textTerminate = QtWidgets.QLabel("Terminate")
        self.textTerminate.setStyleSheet(
            "font-size : 20px;" 
            "background-color : #C2C1C1;"
        )
        self.textTerminate.setAlignment(QtCore.Qt.AlignCenter)
        
        

        for item in self.listeAdd:
            self.listWidget.addItem(item)
            

        layoutList.addWidget(self.listWidget)
        layoutList.addWidget(self.widgetTerminate.listWidgetTerminate)


        layoutText.addWidget(self.textTodo)
        layoutText.addWidget(self.textTerminate)

        layoutButton.addWidget(self.buttonTerminate)
        layoutButton.addWidget(self.buttonDelete)   



        layoutMain.addWidget(self.inputText)
        layoutMain.addWidget(self.buttonAdd)
        layoutMain.addLayout(layoutText)
        layoutMain.addLayout(layoutList)
        layoutMain.addLayout(layoutButton)




        self.setLayout(layoutMain)


        self.widgetTerminate.listWidgetTerminate.itemClicked.connect(self.taskTerminate)
        self.listWidget.itemClicked.connect(self.setItemCurrent)
        self.buttonDelete.clicked.connect(self.deleteItemCurrent)
        self.buttonAdd.clicked.connect(self.add)
        self.buttonTerminate.clicked.connect(self.terminateTask)
        


    @QtCore.Slot()

    def terminateTask(self):

        print("dans la methode terminateTask",self.currentItem)
        self.widgetTerminate.terminateTask(self.currentItem)
        
        current_item = self.currentItem
        self.listeAdd.remove(current_item.text())
        self.listWidget.takeItem(self.listWidget.currentRow()) 
        with open('dataToDo.json', 'w') as f:
            json.dump(self.listeAdd, f)
        

    def taskTerminate(self, item):
        self.ListSelectedItem = "Terminate"
        self.currentItem = item

    def setItemCurrent(self, item):
        self.ListSelectedItem = None
        self.currentItem = item
        print("je suis selectionné apres : ", self.currentItem.text())
    
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
        print("valeur de ListSelectedItem", self.ListSelectedItem)
        current_item = self.currentItem
        print(current_item)
        if current_item is not None:
            if self.ListSelectedItem == "Terminate":
                self.widgetTerminate.listeAddTerminate.remove(current_item.text())
                self.widgetTerminate.listWidgetTerminate.takeItem(self.widgetTerminate.listWidgetTerminate.currentRow()) 
                with open('dataTerminate.json', 'w') as f:
                    json.dump(self.widgetTerminate.listeAddTerminate, f)
            else:
                self.listeAdd.remove(current_item.text())
                self.listWidget.takeItem(self.listWidget.currentRow()) 
                with open('dataToDo.json', 'w') as f:
                    json.dump(self.listeAdd, f)
        else:
            print("No item selected")
        self.currentItem = None
