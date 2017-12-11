'''
Jacob Knecht
Prof. Ordonez
CPTR-215
10/05/17
List GUI Lab 5
'''

from tkinter import *


def addItemtoList(*args):
    addItem = items.get().rstrip()
    if addItem == '':
        pass
    else:
        if items.get() not in itemList:
            itemList.append(items.get())
        sort()
        refresh()


def removeItem(*args):
    temp = gList.get(ACTIVE)
    sort()
    itemList.remove(temp)
    refresh()

def refresh():
    gList.delete(0, END)
    for x in itemList:
        gList.insert(0, x)
    items.set('')

def sort():
    itemList.sort()


items = ''
itemList = []

window = Tk()

Label(window, text='Please enter an item').pack()
items = StringVar()
itemsEntry = Entry(window, textvariable=items)
itemsEntry.pack()
Button(window, text='Add', command=addItemtoList).pack()
Button(window, text='Delete', command=removeItem).pack()
gList = Listbox(window)
gList.pack()

itemsEntry.focus()
window.mainloop()
