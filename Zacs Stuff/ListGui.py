'''
GUI Lab 05
Zacharias Thomas
Fundamentals of Software Design
Professor Ordonez
Date Created: 9/28/2017
Date Last Modified: 9/28/2017
'''

from tkinter import *

def refresh():
    itemBox.delete(0, END)
    for x in itemList:
        itemBox.insert(END, x)
    item.set('')

def addItem(*args):
    localItem = item.get().rstrip()
    if localItem == '':
        item.set('')
        pass
    else:
        if item.get() not in itemList:
            itemList.append(item.get())
        itemCount.append(item.get())
        sortItem()
        refresh()

def sortItem():
    itemList.sort()

def removeItem(*args):
    x = itemBox.get(ACTIVE)
    sortItem()
    itemList.remove(x)
    refresh()

item = ''
itemList = []
itemCount = []

window = Tk()

Label(window, text='Enter an item').pack()
item = StringVar()
itemEntry = Entry(window, textvariable=item)
itemEntry.pack()
Button(window, text='Add', command=addItem).pack()
itemBox = Listbox(window)
itemBox.pack()
Button(window, text='Delete', command=removeItem).pack()

window.bind('<Return>', addItem)
window.bind('<Delete>', removeItem)
itemEntry.focus()
window.mainloop()
