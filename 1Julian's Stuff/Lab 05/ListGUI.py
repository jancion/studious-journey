'''
Julian Ancion
Prof. Ordonez
CPTR-215
10/5//2017
ListGUI.py
Simple gui to add, remove and sort a list passed to it.
'''

from tkinter import *



def add_list(*args):
    '''
    takes the item in the text box, checks if it is already in the list and if not present,
    adds item to the lets,, else ignores it.
    :param args: placeholder so it does not break program
    :return: returns nothing.
    '''
    temp_item = item.get().rstrip()
    if temp_item == '':
        item.set('')
    else:
        if item.get() not in items:
            items.append(item.get())

        sort()
        refresh()


def remove(*args):
    '''
    removes the active ( underlined ) item from the list with the delete button is pressed
     or when the delete key is pressed on keyboard.
    :param args: placeholder so it does not break program
    :return: returns nothing.
    '''
    i = list_box.get(ACTIVE)
    sort()
    items.remove(i)
    refresh()


def sort():
    '''
    Really complicated sort function.
    :return: returns nothing
    '''
    items.sort()


def refresh():
    '''
    updates the list after items are added or deleted.
    :return: you guessed it, nothing is returned
    '''
    list_box.delete(0, END)
    for i in items:
        list_box.insert(END, i)
    item.set('')



'''
The rest builds the GUI and activates the buttons and functions
'''
item = ''
items = []


window = Tk()

Label(window, text='Enter an item').pack()
item = StringVar()
entry_box = Entry(window, textvariable=item)
entry_box.pack()
Button(window, text='Enter', command=add_list).pack()
list_box = Listbox(window)
list_box.pack()
Button(window, text='Delete', command=remove).pack()

window.bind('<Return>', add_list)
window.bind('<Delete>', remove)
entry_box.focus()
window.mainloop()
