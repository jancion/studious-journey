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
    avg_paragraphs = words / paragraphs
    easy_reading = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
    fk_grade = 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59
    gfi = .4 * (words / sentences) + 100 * (complex / words)

    # chars += lines
    letters = "Letters:", str(letters)
    words = "Words:", str(words)
    syllables = "Syllables:", str(syllables)
    sentences = "Sentences:", str(sentences)
    avg_syllable = "Average syllables per word:", str(avg_syllable)
    avg_word = "Average word length:", str(avg_word)
    avg_sentence = "Average sentence word length:", str(int(avg_sentence))
    paragraphs = "Paragraphs:", str(paragraphs)
    avg_paragraphs = "Average words per paragraph:", str(int(avg_paragraphs))
    easy_reading = "Easy-reading:", str(int(easy_reading))
    gfi = "Gunning-Fog Index:", str(int(gfi))
    fk_grade = "Flesch-Kincaid:", str(int(fk_grade))

    sentences_label.set(sentences)
    word_label.set(words)
    letters_label.set(letters)
    syllables_label.set(syllables)
    avg_word_label.set(avg_word)
    avg_syllable_label.set(avg_syllable)
    avg_sentence_label.set(avg_sentence)
    paragraphs_label.set(paragraphs)
    paragraph_len_label.set(avg_paragraphs)
    easy_reading_label.set(easy_reading)
    gfi_label.set(gfi)
    fk_grade_label.set(fk_grade)


# window

window.geometry("400x350")
window.title("TextFileGUI.py")
text = StringVar()
text.set('Please select a file:')
Label(textvariable=text, width=20).pack()
new_file = Button(text='Select File', width=5, command=readfile).pack()
sentences_label = StringVar()
letters_label = StringVar()
word_label = StringVar()
syllables_label = StringVar()
avg_word_label = StringVar()
avg_syllable_label = StringVar()
avg_sentence_label = StringVar()
paragraphs_label = StringVar()
paragraph_len_label = StringVar()
easy_reading_label = StringVar()
gfi_label = StringVar()
fk_grade_label = StringVar()

Label(textvariable=letters_label).pack()
Label(textvariable=word_label).pack()
Label(textvariable=sentences_label).pack()
Label(textvariable=syllables_label).pack()
Label(textvariable=avg_sentence_label).pack()
Label(textvariable=paragraphs_label).pack()
Label(textvariable=paragraph_len_label).pack()
Label(textvariable=easy_reading_label).pack()
Label(textvariable=gfi_label).pack()
Label(textvariable=fk_grade_label).pack()

# enables window mainloop
window.mainloop()
