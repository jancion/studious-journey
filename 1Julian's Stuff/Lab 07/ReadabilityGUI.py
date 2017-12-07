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

def syllable_count(word):
    # inspired by https://codegolf.stackexchange.com/a/47325
    import re
    count = len(re.split("[aiouy]+e*|e(?!d$|ly).|[td]ed|le$", word.lower())) - 1
    return count if count > 0 else 1


def readfile(*args):
    '''
    *** initialdir MUST be changed when activated on non UNIX computer.
    Selects and reads the file and outputs the line, word and character counts into a GUI
    :param args: place holder to prevent errors
    :return: returns nothing
    '''
    window.file = filedialog.askopenfile(initialdir="/", title="Select file",
                                              filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    lines = words = chars = letters = syllables = sentences =  paragraphs = complex = 0
    for line in window.file:
        lines += 1
        for i in line:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letters += 1
            if i in "?.!":
                sentences += 1


        chars += len(line)
        words += len(line.split())
        word_list = line.split(" ")
        for i in word_list:
            syllables += syllable_count(i)
            if syllable_count(i) > 3 and i[-2:] != 'ed' and i[-2:] != 'es' and i[-3] != 'ing':
                complex += 1
        if word_list[-1] == '\n':
            paragraphs += 1
    # Enable to work on other computers/files
    avg_word = letters / words
    avg_sentence = words / sentences
    avg_syllable = syllables / words
    gfi = .4((words / sentences) + 100 (complex / words))

    print(letters)
    print(syllables)
    print(sentences)
    print(avg_syllable)
    print(avg_word)
    print(avg_sentence)
    print(paragraphs)
    print(complex)
    print(gfi)



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
