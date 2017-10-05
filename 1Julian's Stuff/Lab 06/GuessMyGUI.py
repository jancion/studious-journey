'''
Julian Ancion
Prof. Ordonez
C{TR-215
10/5/17
Simple guessing game.
'''

# imports modules from python
from tkinter import *
import math

# enables the Tk() module and sets a few global variables
gui = Tk()
mid_num = 0
range_min = 0
range_max = 0
guesses = 0
max_guess = 0


def higher():
    '''
    This function is run when the user presses the higher button.
    Recalculates the min range and asks the user for input again.
    :return: nothing is returned
    '''
    global mid_num, range_min, range_max, guesses, guess_text
    guesses += 1
    range_min = mid_num
    mid_num = math.ceil((int(range_min) + int(range_max)) / 2)
    temp = ('Is your number:' + str(mid_num))
    text.set(temp)


def lower():
    '''
    This function is run when the user presses the lower button.
    Recalculates the max range and asks the user for input again.
    :return: Nothing is returned
    '''
    global mid_num, range_min, range_max, guesses, guess_text
    guesses += 1
    range_max = mid_num
    mid_num = math.floor((int(range_min) + int(range_max)) / 2)
    temp = ('Is your number:' + str(mid_num))
    text.set(temp)


def correct():
    '''
    This function is run if the user selects correct.
    it displays the message 'I win!' nad checks to see if it guessed in fewer than the max guesses.
    If it is fewer it displays the popup containing the amount of guesses used.
    :return: nothing is returned
    '''
    global guesses
    guesses += 1
    if guesses < max_guess:
        popup = Toplevel()
        popup_label = Label(popup, text='I used ' + str(guesses) + ' out of ' + str(max_guess) + ' guesses.').pack()
    text.set('I win')


def set_range():
    '''
    Sets the range and removes the boxes associated with it.
    It then enables the guessing button options to select whether it is higher, lower or correct.
    :return:
    '''
    global mid_num, range_max, range_min, max_guess
    range_min = int(min_entry.get())
    range_max = int(max_entry.get())
    text.set('Guessing!')
    min_entry.destroy()
    max_entry.destroy()
    range_enter.destroy()
    mid_num = (int(range_min) + int(range_max)) // 2
    higher_button = Button(text='Higher', width=5, height=1, command=higher)
    higher_button.place(x=75, y=110)
    lower_button = Button(text='Lower', width=5, height=1, command=lower)
    lower_button.place(x=275, y=110)
    correct_button = Button(text='Got it!', width=5, height=1, command=correct)
    correct_button.place(x=175, y=110)
    temp = ('Is your number:' + str(mid_num))
    text.set(temp)
    max_guess = math.ceil(math.log(range_max, 2))


# gui
gui.geometry("400x150")
gui.title("Guess my number!")
guess_text = ''
text = StringVar()
text.set('Enter a range(min, max)')
Label(textvariable=text, width=20).pack()
Label(textvariable=guess_text)

# range entry boxes and button initialization
min_entry = Entry(width=5)
max_entry = Entry(width=5)
min_entry.place(x=122, y=25)
max_entry.place(x=222, y=25)
min_entry.insert(END, 1)
max_entry.insert(END, 100)
range_enter = Button(text='Enter Range', width=10, command=set_range)
range_enter.place(x=145, y=50)

# enables gui mainloop
gui.mainloop()
