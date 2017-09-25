#test gui

from tkinter import *

def greet(*args):
    greetingVar.set("Hello, " + nameVar.get())

window = Tk()
Label(window, text = "What's your name?").pack()
nameVar = StringVar()
nameEntry = Entry(window, textvariable = nameVar)
nameEntry.pack()
Button(window, text = "Click me!", command = greet).pack()
greetingVar = StringVar()
greeting = Label(window, text = "Greeting here").pack()
Label(window, textvariable = greetingVar).pack()

nameEntry.focus()
window.bind("<Entry>", greet)



window.mainloop()
