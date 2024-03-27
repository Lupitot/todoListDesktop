import json
from PySide6 import QtCore, QtWidgets


class WidgetTerminateTask(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.currentItemTerminate = None
        

        try:
            with open('dataTerminate.json', 'r') as f:
                self.listeAddTerminate = json.load(f)
        except FileNotFoundError:
            self.listeAddTerminate = []

        self.listWidgetTerminate = QtWidgets.QListWidget()
        self.listWidgetTerminate.setStyleSheet(
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
        self.listWidgetTerminate.setSpacing(5)



        for task in self.listeAddTerminate:
            self.listWidgetTerminate.addItem(task)


    def terminateTask(self, currentItem):
        self.currentItemTerminate = currentItem

        if self.currentItemTerminate is None:
            return
            

        self.listeAddTerminate.append(self.currentItemTerminate.text())
        print(self.listeAddTerminate)
            
        with open('dataTerminate.json', 'w') as f:
            json.dump(self.listeAddTerminate, f)


            

        self.updateListWidget()

    def updateListWidget(self):
        self.listWidgetTerminate.clear()

        for item in self.listeAddTerminate:
            self.listWidgetTerminate.addItem(item)
