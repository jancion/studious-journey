from tkinter import *
import math
guess = 0
guesscounter = 0
maxguess = 0
def guessHigher(*args):
    #guess higher
    global guess, guesscounter
    minimum.set(guess + 1)
    guess = guess + math.ceil((maximum.get() - guess) / 2)
    initialLabel.set("Is this your number: " + str(guess) + "?")
    guesscounter += 1


def guessLower(*args):
    #guess lower
    global guess, guesscounter
    maximum.set(guess - 1)
    guess = guess - math.ceil((guess - minimum.get()) / 2)
    initialLabel.set("Is this your number: " + str(guess) + "?")
    guesscounter += 1


def guessCorrect():
    global guesscounter, maxguess
    guesscounter = str(guesscounter)
    tkGuessCounter = StringVar()
    tkGuessCounter.set("I guessed " + guesscounter + " times out of " + str(maxguess) + " times.")
    toplevel = Toplevel()
    toplevel.geometry("300x100")
    if guesscounter < maxguess:
        label1 = Label(toplevel, text="I have super smarts!!!", height=5, width=10)
        label1.pack()
    else:
        label1 = Label(toplevel, text="I have average smarts.", height=5, width=10)
        label1.pack()
    label2 = Label(toplevel, textvariable=tkGuessCounter)
    label2.pack()

def destroyEverything(*args):
    global guess, guesscounter, maxguess
    minEntry.destroy()
    maxEntry.destroy()
    cButton.destroy()
    hButton = Button(window, text="Higher", command=guessHigher, width=5, height=2)
    hButton.place(x=75, y=150)
    lButton = Button(window, text="Lower", width=5, height=2, command=guessLower)
    lButton.place(x=275, y=150)
    correctButton = Button(window, text="Correct", width=5, height=2, command=guessCorrect)
    correctButton.place(x=175, y=150)
    maxguess = math.ceil(math.log((maximum.get() - minimum.get()), 2))
    guess = maximum.get() - (math.ceil((maximum.get() - minimum.get()) / 2))
    initialLabel.set("Is this your number: " + str(guess) + "?")
    guesscounter += 1


window = Tk()
window.geometry('400x200')
minimum = IntVar()
maximum = IntVar()
divideInt = IntVar()
maximum.set(100)
minimum.set(1)
initialLabel = StringVar()
initialLabel.set('Please enter the range of the number you are thinking.\nMinimum on top, maximum on bottom.')
Label(window, textvariable = initialLabel).pack()

minEntry = Entry(window, textvariable=minimum, width=5)
minEntry.place(x=130, y=85)
maxEntry = Entry(window, textvariable=maximum, width=5)
maxEntry.place(x=230, y=85)

cButton = Button(window, text="Continue", command=destroyEverything)
cButton.place(x=160, y=135)



window.mainloop()