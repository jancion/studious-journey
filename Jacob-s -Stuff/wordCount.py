from tkinter import filedialog
from tkinter import *
#This code was developed by Jacob Knecht
def countEverything():
    #Counts lines, words, and characters
    lineCounter.set(0)
    for line in window.file:
        #Line counter
        lineCounter.set(lineCounter.get() + 1)
        #Character length
        charCounter.set(charCounter.get() + len(line))
        #Word list
        wordCounter.set(wordCounter.get() + len(line.split()))
    printResults()

def printResults():
    openButton.destroy()
    initialLabel.set('Here are my results')
    lineResults.set('There were ' + str(lineCounter.get()) + ' lines.')
    Label(window, textvariable=lineResults, height=3).pack()
    wordResults.set('There were ' + str(wordCounter.get()) + ' words.')
    Label(window, textvariable=wordResults, height=3).pack()
    charResults.set('There were ' + str(charCounter.get()) + ' characters.')
    Label(window, textvariable=charResults, height=3).pack()

def openFile():
    #Opens file and assigns it
    window.file = filedialog.askopenfile(initialdir="/", title="Select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    countEverything()
    window.file.close()

window = Tk()
window.geometry('400x200')
window.title('Word Counter')
initialLabel = StringVar()
lineCounter = IntVar()
lineResults = StringVar()
wordCounter = IntVar()
wordResults = StringVar()
charCounter = IntVar()
charResults = StringVar()
initialLabel.set('Please open a file, so I may count them words!')
Label(window, textvariable=initialLabel).pack()

openButton = Button(window, text="Open", width=5, height=2, command=openFile)
openButton.place(x=175, y=100)

window.mainloop()