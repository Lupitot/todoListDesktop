import json
import os
import time
from colorama import Fore, Style


class Console:


    # Debut de l'application
    def start(self):
        self.clearTerminal()
        print(Style.RESET_ALL)
        print(Style.BRIGHT + Fore.BLUE + "\n====== Welcom in your To-Do List ======\n")
        self.choice()

    # Effacer le terminal
    def clearTerminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Gestion des choix de l'utilisateur
    def choice(self):
        print(Style.RESET_ALL)
        print("1- Add a task")
        print("2- Show all tasks not finished")
        print("3- Show all task finished")
        choice = input("\nEnter your choice: ")
    
        if choice == "1":
            task = input(Style.BRIGHT + "\n======= Enter your task =======\n")
            print(Style.RESET_ALL)
            self.addTask(task)
        elif choice == "2":
            self.showTaskNotFinished()
        elif choice == "3":
            self.showTaskFinished()
        
        self.start()

    # Ajouter une tâche
    def addTask(self, task):
        self.clearTerminal()
        allTasks = []

        # Charger les tâches non terminées
        with open('dataToDo.json', 'r') as f:
            data = f.read()
            if data:
                allTasks = json.loads(data)
                if not isinstance(allTasks, list):
                    allTasks = []

        # ajouter la tache a la liste
        allTasks.append(task)
        with open('dataToDo.json', 'w') as f:
            json.dump(allTasks, f)
        print(Fore.GREEN + "\n\n\n===== Task added successfully =====\n")
        time.sleep(1)

    # afficher les tâches non terminées
    def showTaskNotFinished(self):
        print(Style.RESET_ALL)
        self.clearTerminal()
        with open('dataToDo.json', 'r') as f:
            data = f.read()

        print(Style.BRIGHT + Fore.BLUE+ "\n======= Your tasks not finished =======\n")
        print(Style.RESET_ALL)
        for i, task in enumerate(json.loads(data)):
            print(f"{i+1}- {task}")

        self.otherChoice("taskNotFinished")

    # afficher les tâches terminées
    def showTaskFinished(self):
        print(Style.RESET_ALL)
        self.clearTerminal()
        with open('dataTerminate.json', 'r') as f:
            data = f.read()
        
        print(Style.BRIGHT + Fore.BLUE +  "\n======= Your tasks finished =======\n")
        print(Style.RESET_ALL)
        for i, task in enumerate(json.loads(data)):
            print(f"{i+1}- {task}")

        
        self.otherChoice("taskFinished")

    # Definir une tâche comme terminée
    def addTaskFinished(self, index):
        allTasks = []
        allTasksFinished = []

        # Charger les tâches terminées
        with open('dataTerminate.json', 'r') as f:
            data = f.read()
            if data:
                allTasksFinished = json.loads(data)
                if not isinstance(allTasksFinished, list):
                    allTasksFinished = []
        
        # Charger les tâches non terminées
        with open('dataToDo.json', 'r') as f:
            data = f.read()
            if data:
                allTasks = json.loads(data)
                if not isinstance(allTasks, list):
                    allTasks = []
        
        # Terminer la tâche si l'index est valide
        if index < len(allTasks):
            task = allTasks[index]
            allTasks.remove(task)
            allTasksFinished.append(task)
            with open('dataToDo.json', 'w') as f:
                json.dump(allTasks, f)
            with open('dataTerminate.json', 'w') as f:
                json.dump(allTasksFinished, f)
            print(Fore.GREEN +  "Task finished")
            time.sleep(1)

        self.showTaskNotFinished()

    # Gestion des choix secondaires lors de l'affichage des tâches
    def otherChoice(self, currentTask = None):
        print(Style.BRIGHT + Fore.BLUE +  "\n=======================================\n")
        print(Style.RESET_ALL)

        # Gestion affichage des choix en fonction des taches affichées
        listOptions = ["Finish a task", "Delete a task", "Back"]
        if currentTask == "taskFinished":
            listOptionsWithoutFinish = [option for option in listOptions if option != "Finish a task"]
            for i in range(len(listOptionsWithoutFinish)):
                print(f"{i+1}- {listOptionsWithoutFinish[i]}")
        else: 
            for i in range(len(listOptions)):
                print(f"{i+1}- {listOptions[i]}")

        # Gestion des choix de l'utilisateur
        try: 
            choice = int(input("\nEnter your choice: "))
            # Gestion du choix 1 en fonction des tâches affichées
            if choice == 1 and currentTask == "taskNotFinished":
                # Choix de la tâche à terminer
                try:
                    index = int(input("\nEnter the number of the task to finish: "))
                    if int(index) > 0 :
                        self.addTaskFinished(int(index)-1)
                except ValueError:
                    print(Fore.RED + "Invalid index")
                    time.sleep(1)
                    self.showTaskFinished()
            elif choice == 1 and currentTask == "taskFinished":
                # choix de la tache a supprimer
                try:
                    index = int(input("\nEnter the number of the task to delete: "))
                    if int(index) > 0 :
                        self.deleteTask(int(index)-1, currentTask)
                except ValueError:
                    print(Fore.RED + "Invalid index")
                    time.sleep(1)
                    currentTask == "taskFinished"
                    self.showTaskFinished()
            # Gestion du choix 2 en fonction des tâches affichées
            elif choice == 2 and currentTask == "taskNotFinished":
                # choix de la tache a supprimer
                try:
                    index = int(input("\nEnter the number of the task to delete: "))
                    if int(index) > 0 :
                        self.deleteTask(int(index)-1, currentTask)
                except ValueError:
                    print(Fore.RED + "Invalid index")
                    time.sleep(1)
                    if currentTask == "taskNotFinished":
                        self.showTaskNotFinished()
            elif choice == 2 and currentTask == "taskFinished":
                # Retour au menu principal
                self.start()

        except ValueError:
            print(Fore.RED + "Invalid choice")
            time.sleep(1)
            if currentTask == "taskNotFinished":
                self.showTaskNotFinished()
            elif currentTask == "taskFinished":
                self.showTaskFinished()
    
    # Supprimer une tâche
    def deleteTask(self, index, listCurrentTask = None):
        allTasks = []
        finishedTasks = []
        
        if listCurrentTask == "taskNotFinished":
            # Charger les tâches non terminées
            with open('dataToDo.json', 'r') as f:
                data = f.read()
                if data:
                    allTasks = json.loads(data)
                    if not isinstance(allTasks, list):
                        allTasks = []
            # Supprimer la tâche si l'index est valide pour les tâches non terminées
            if index < len(allTasks):
                task = allTasks.pop(index)
                with open('dataToDo.json', 'w') as f:
                    json.dump(allTasks, f)
                print(f"Task '{task}' deleted from unfinished tasks")

                self.showTaskNotFinished()
            else:
                print(Fore.RED + "Invalid index")

        elif listCurrentTask == "taskFinished":
            # Charger les tâches terminées
            with open('dataTerminate.json', 'r') as f:
                data = f.read()
                if data:
                    finishedTasks = json.loads(data)
                    if not isinstance(finishedTasks, list):
                        finishedTasks = []

            # Supprimer la tâche si l'index est valide pour les tâches terminées
            if index < len(finishedTasks):
                task = finishedTasks.pop(index)
                with open('dataTerminate.json', 'w') as f:
                    json.dump(finishedTasks, f)
                print(f"Task '{task}' deleted from finished tasks")

                self.showTaskFinished()
            else:
                print(Fore.RED + "Invalid index")


console = Console()
console.start()