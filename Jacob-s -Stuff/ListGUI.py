from tkinter import *

def addItemtoList(*args):
    addItem = items.get().rstrip()
    if addItem == '':
        pass
    else:
        gList.insert(END, addItem)
        gList.sort()

def removeItem(*args):
    pass

itemList = []

window = Tk()

Label(window, text='Please enter an item').pack()
items = StringVar()
itemsEntry = Entry(window, textvariable=items)
itemsEntry.pack()
Button(window, text='Add', command=addItemtoList).pack()
gList = Listbox(window)
gList.pack()
itemsEntry.focus()
window.mainloop()