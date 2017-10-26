'''
5c-gui-play.py
Julian Ancion && Robert Ordonez
2017-09-25 just a window
'''
from tkinter import *

itemList = []

def addListItem(*args):
    itemList.append(args)


def removeListItem(*args):
    pass


def sortListItem(*args):
    pass

def ListBox(*args):
    pass

'''
def GreetingBox(*args):
    if nameVar.get() == "Zac Thomas":
        greetingVar.set("Stop touching my stuff.")
    else:
        greetingVar.set("Howdy, " + nameVar.get())
    print(args)
'''

window = Tk()
Label(window, text="Enter list item and press enter: ").pack()
itemVar = StringVar()
nameEntry = Entry(window, textvariable=itemVar)
nameEntry.pack()
Button(window, text="Add Item", command=addListItem(itemVar)).pack()
itemVar = StringVar()
Label(window, textvariable=itemVar).pack()
print(itemVar)
print(itemList)
nameEntry.focus()
window.bind("<Return>", ListBox)
window.mainloop()
