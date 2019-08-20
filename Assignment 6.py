### Author - Tommy Aguilu
### Version 1.0
### Class - Foundations of Programing

d = {} #creat dict and then open current iteration of to do list
with open("todo.txt") as f: #opens the text file as variable f
    for line in f:
        x = line.split(",")
        a = x[0]
        b = x[1]
        c = len(b)-1 #cleans /n in text files by slicing off the /n input
        b = b[0:c]
        d[a] = b

### creation of class for menu functions
class menu_overlay:
    @staticmethod
    def show_todo():
        print("Current To Do List")
        for key, value in d.items():
            print(key, value)
        print("")
    @staticmethod
    def menu():
        print("please make a selection")
        menu = {"1:" : "Show current to do list", "2:" : "Add new item to the list", "3:" : "Finish a task ", "4:" : "Exit"}
        for key, value in menu.items():
            print(key, value)
        print("")
        return menu
    @staticmethod
    def remove():
        delete_input = input("what would you like to complete? ")
        try:
            del d[delete_input]
            print("Good job at finishing " + delete_input + "!")
        except KeyError:
            print("Task not found in list")
    @staticmethod
    def add_item(d):
        ###returns dictionary
        new_task = dict()
        task = input("what do you need to do? ")
        priority = input("whats the priority? (high or low)")
        new_task[task] = priority
        d = dict(d, **new_task)
        return d

menu_overlay().show_todo()
menu_overlay().menu()
loop = True
while loop == True:
    choice = input("what would you like to do? (1, 2, 3, 4)")
    if choice == "1":
        menu_overlay.show_todo()
    if choice == "2":
        d = menu_overlay.add_item(d)
        menu_overlay.show_todo()
    if choice == "3":
        menu_overlay.remove()
        menu_overlay.show_todo()
    if choice == "4":
        menu_overlay.show_todo()
        loop = False
        with open("todo.txt","w") as g:
            for key, value in d.items():
                g.write('%s,%s\n' % (key, value))
