from tkinter import filedialog
from tkinter import *
#This code was developed by Jacob Knecht
def syllableCount(word):
    # inspired by https://codegolf.stackexchange.com/a/47325
    import re
    count = len(re.split("[aiouy]+e*|e(?!d$|ly).|[td]ed|le$", word.lower())) - 1
    return count if count > 0 else 1

def countEverything():
    for line in window.file:
        #syllable counter and complex word counter
        wordList = line.split()
        for x in wordList:
            syllCounter.set(syllCounter.get() + syllableCount(x))
            if 'es' in x[-2:]:
                x = x.replace('es', '')
            elif 'ed' in x[-2:]:
                x = x.replace('ed', '')
            elif 'ing' in x[-3:]:
                x = x.replace('ing', '')
            if '.' in x:
                if 'es' in x[-3:]:
                    x = x.replace('es', '')
                if 'ed' in x[-3:]:
                    x = x.replace('ed', '')
                elif 'ing' in x[-4:]:
                    x = x.replace('ing', '')
            complexCheck = syllableCount(x)
            if complexCheck >= 3:
                complexCounter.set(complexCounter.get() + complexCheck)
        #Word list
        wordCounter.set(wordCounter.get() + len(line.split()))
        #sentence counter
        sentCounter.set(sentCounter.get() + line.count('.') + line.count('!') + line.count('?'))
    readability()


def readability():
    import math
    #Flesch reading ease
    flesch = 206.835 - 1.015*(wordCounter.get() / sentCounter.get()) - 84.6*(syllCounter.get() / wordCounter.get())
    #print(round(flesch, 2))
    if 100 >= flesch >= 90.01:
        schoolLevel = "5th grade"
    if 90 >= flesch >= 80.01:
        schoolLevel = "6th grade"
    if 80 >= flesch >= 70.01:
        schoolLevel = "7th grade"
    if 70 >= flesch >= 60.01:
        schoolLevel = "8th grade & 9th grade"
    if 60 >= flesch >= 50.01:
        schoolLevel = "10th grade to 12th grade"
    if 50 >= flesch >= 30.01:
        schoolLevel = "College level"
    if 30 >= flesch >= 0:
        schoolLevel = "College graduate level"
    if flesch < 0:
        schoolLevel = "Prodigy level"
    fleschStr.set('This book is at a ' + schoolLevel + ' with a score of ' + str(round(flesch, 2)) + '.')
    Label(window, text="Flesch reading ease").pack()
    Label(window, textvariable=fleschStr).pack()
    #Flesh-Kincaid grade level
    kincaid = 0.39*(wordCounter.get() / sentCounter.get()) + 11.8*(syllCounter.get() / wordCounter.get()) - 15.59
    if math.floor(kincaid) <= 0:
        schoolLevel = "Kindergarten"
    else:
        schoolLevel = "Grade "+ str(math.floor(kincaid))
    kincaidStr.set('This book is an ' + schoolLevel + ' with a score of ' + str(round(kincaid, 2)))
    Label(window, text="Flesch-Kincaid grade level").pack()
    Label(window, textvariable=kincaidStr).pack()
    #Gunning fog index
    fogdict = {17 : "College graduate",
               16 : "College senior",
               15 : "College junior",
               14 : "College Sophomore",
               13: "College Freshman",
               12: "High school senior",
               11: "High school junior",
               10: "High school sophomore",
               9: "High school freshmeat",
               8: "Eighth grade",
               7: "Seventh grade",
               6: "Sixth grade"}
    fog = 0.4*((wordCounter.get() / sentCounter.get()) + 100*(complexCounter.get() / wordCounter.get()))
    print(fog)
    fogStr.set('This book has a reading level of a/an ' + fogdict[math.floor(fog)] + ' with a score of ' + str(round(fog, 2)))
    Label(window, text="Gunning fog index").pack()
    Label(window, textvariable=fogStr).pack()


def openFile():
    #Opens file and assigns it
    window.file = filedialog.askopenfile(initialdir="/", title="Select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    openButton.destroy()
    initialLabel.set('Here are my results')
    countEverything()
    window.file.close()

window = Tk()
window.geometry('500x200')
window.title('Readability Counter')
initialLabel = StringVar()
fleschStr = StringVar()
kincaidStr = StringVar()
fogStr = StringVar()
#complex word counter
complexCounter = IntVar()
#word counter
wordCounter = IntVar()
#syllable counter
syllCounter = IntVar()
#sentence counter
sentCounter = IntVar()
initialLabel.set('Please open a file, so I may check the readability of the document!')
Label(window, textvariable=initialLabel).pack()

openButton = Button(window, text="Open", width=5, height=2, command=openFile)
openButton.place(x=175, y=100)

window.mainloop()