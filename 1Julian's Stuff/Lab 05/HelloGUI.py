'''
HelloGui.py
Julian Ancion && Robert Ordonez
2017-09-28
'''
from tkinter import *


def GreetingBox(*args):
    if nameVar.get() == "Zac Thomas":
        greetingVar.set("Stop touching my stuff.")
    else:
        greetingVar.set("Howdy, " + nameVar.get())
    print(args)


window = Tk()
Label(window, text="Enter Your name: ").pack()
nameVar = StringVar()
nameEntry = Entry(window, textvariable=nameVar)
nameEntry.pack()
Button(window, text="DO IT", command=GreetingBox).pack()
greetingVar = StringVar()
Label(window, textvariable=greetingVar).pack()

nameEntry.focus()
window.bind("<Return>", GreetingBox)
window.mainloop()
