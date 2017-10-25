'''
Julian Ancion
Prof. Ordonez
CPTR-215-A
10/19/2017
TextFilewindow.py
'''


from tkinter import filedialog
from tkinter import *


window = Tk()
file_name = ''


def readfile(*args):
    '''
    *** initialdir MUST be changed when activated on non UNIX computer.
    Selects and reads the file and outputs the line, word and character counts into a GUI
    :param args: place holder to prevent errors
    :return: returns nothing
    '''
    window.file = filedialog.askopenfile(initialdir="/", title="Select file",
                                              filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    lines = words = chars = 0
    for line in window.file:
        lines += 1
        chars += len(line)
        words += len(line.split())
    # Enable to work on other computers/files
    # chars += lines
    lines = "Lines:", str(lines)
    words = "Words:", str(words)
    chars = "Characters:", str(chars)
    line_label.set(lines)
    word_label.set(words)
    char_label.set(chars)


# window
window.geometry("400x150")
window.title("TextFileGUI.py")
text = StringVar()
text.set('Please select a file:')
Label(textvariable=text, width=20).pack()
new_file = Button(text='Select File', width=5, command=readfile).pack()
line_label = StringVar()
char_label = StringVar()
word_label = StringVar()
Label(textvariable=line_label, width=20).pack()
Label(textvariable=word_label, width=20).pack()
Label(textvariable=char_label, width=20).pack()


# enables window mainloop
window.mainloop()
