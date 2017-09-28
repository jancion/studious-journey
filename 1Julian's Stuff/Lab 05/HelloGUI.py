# 5c-gui-play.py
# Robert Ordóñez & CPTR-215
# 2017-09-25 just a window

from tkinter import *


def HelloGUI(*args):
    if nameVar.get() == "Zac Thomas":
        greetingVar.set("Stop touching my stuff.")
    else:
        greetingVar.set("Hello, " + nameVar.get())
    print(args)


window = Tk()
Label(window, text="What's your name?").pack()
nameVar = StringVar()
nameEntry = Entry(window, textvariable=nameVar)
nameEntry.pack()
Button(window, text="Greet me!", command=HelloGUI).pack()
greetingVar = StringVar()
Label(window, textvariable=greetingVar).pack()

nameEntry.focus()
window.bind("<Return>", HelloGUI)
window.mainloop()
