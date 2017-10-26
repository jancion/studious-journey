'''
HelloGui.py
Julian Ancion && Robert Ordonez
2017-09-28
Runs a small GUI that accepts input for a name and
returns a statement saying Howdy, <username>
or an easter egg for Zac Thomas.
'''
from tkinter import *


def greetingBox(*args):
    '''
    Checks the nameVar and if equal to 'Zac Thomas'
    it sets greetingVar to "Stop touching my stuff"
    else sets greetingVar to Howdy, <name entered>.
    '''
    if nameVar.get() == "Zac Thomas":
        greetingVar.set("Stop touching my stuff.")
    else:
        greetingVar.set("Howdy, " + nameVar.get())
    nameVar.set('')


window = Tk()
Label(window, text="Enter Your name: ").pack()
nameVar = StringVar()
nameEntry = Entry(window, textvariable=nameVar)
nameEntry.pack()
Button(window, text="Enter", command=greetingBox).pack()
greetingVar = StringVar()
Label(window, textvariable=greetingVar).pack()

nameEntry.focus()
window.bind("<Return>", greetingBox)
window.mainloop()
