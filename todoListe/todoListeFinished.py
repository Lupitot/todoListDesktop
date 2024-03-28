import json
from PySide6 import QtCore, QtWidgets


# Widget pour les tâches terminées
class WidgetFinishedTask(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.currentItemFinished = None
        

        try:
            with open('../dataTerminate.json', 'r') as f:
                self.listeAddFinished = json.load(f)
        except FileNotFoundError:
            self.listeAddFinished = []

        self.listWidgetFinished = QtWidgets.QListWidget()
        self.listWidgetFinished.setStyleSheet(
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
        self.listWidgetFinished.setSpacing(5)



        for task in self.listeAddFinished:
            self.listWidgetFinished.addItem(task)


    def finishedTask(self, currentItem):
        self.currentItemFinished = currentItem

        if self.currentItemFinished is None:
            return
            

        self.listeAddFinished.append(self.currentItemFinished.text())
        print(self.listeAddFinished)
            
        with open('dataTerminate.json', 'w') as f:
            json.dump(self.listeAddFinished, f)


            

        self.updateListWidget()

    def updateListWidget(self):
        self.listWidgetFinished.clear()

        for item in self.listeAddFinished:
            self.listWidgetFinished.addItem(item)
