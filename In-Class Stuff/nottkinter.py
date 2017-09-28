# 5c-gui-play.py
# Robert Ordóñez & Julian Ancion
# 2017-09-25 just a window


from tkinter import *


def HelloGUI(*args):
    greetingVar.set("Hello, " + nameVar.get())
    print(args)


window = Tk()


Label(window, text="What's your name?").pack()
nameVar = StringVar()
nameEntry = Entry(window, textvariable=nameVar)
nameEntry.pack()
Button(window, text="Greet me!", command=greet).pack()
greetingVar = StringVar()
Label(window, textvariable=greetingVar).pack()
Label(window, text="You've been typing:").pack()
Label(window, textvariable=nameVar).pack()

nameEntry.focus()
window.bind("<Return>", greet)
window.mainloop()


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    from random import randint
    secret_number = randint(1, 100)
    print('I\'m thinking of a number between 1 and 100.')
    guess = -1
    while guess != secret_number:
        guess = int(input('Your guess: '))
        if guess == secret_number:
            print('you got it!')
        elif guess > secret_number:
            print('lower.')
        else:
            print('higher')



