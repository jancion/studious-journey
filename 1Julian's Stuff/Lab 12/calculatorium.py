'''
Julian Ancion
Prof. Ordonez
CPTR-215
Calculator
'''
from tkinter import *


class CalculatorGuts:
    '''
    '''

    def __init__(self, *args):
        self.left_operand = '0'
        self.pending_operator = ''
        self.display = '0'
        self.start_new_number = True
        self.decimal_flag = False
        self.num_list = '0123456789.'
        self.operator_list = '+-*/='
        self.inverse_list = '$'
        self.clear_list = 'c'
        self.part_clear = 'ce'

    def __repr__(self):
        return "%s" % (self.display)

    def button_pressed(self, button):
        if button in self.num_list:
            self.number_pressed(button)
        elif button in self.operator_list:
            self.operator_pressed(button)
        elif button == self.inverse_list:
            self.inverse()
        elif button == self.clear_list:
            self.clear()
        elif button == self.part_clear:
            self.partial_clear()

    def number_pressed(self, button):
        if button == '.':
            if '.' in self.display:
                pass
            else:
                self.decimal_flag = True
                self.display += '.'
        if self.start_new_number is True:
            # Fresh calculator just turned on, replaces '0.' with pressed number
            self.display = button
            self.start_new_number = False
        else:
            # appends pressed button to number
            self.display += button
        self.decimal_check()

    def operator_pressed(self, button):
        if self.start_new_number is True:
            # if '0.' and fresh number, have it do nothing if = is pressed
            if button == '=':
                self.decimal_check()
            else:
                # numbers have already been put in.
                self.pending_operator = button
        else:
            # after operand is assigned
            if button == "=":
                self.evaluate()
                self.pending_operator = ''
            else:
                if self.pending_operator == '':
                    self.left_operand = self.display
                    self.pending_operator = button
                    self.start_new_number = True
                    self.decimal_flag = False
                else:
                    self.evaluate()
                    self.left_operand = self.display
                    self.decimal_flag = False
                    self.start_new_number = True

    def evaluate(self):
        if self.pending_operator == "+":
            self.add()
        if self.pending_operator == "-":
            self.sub()
        if self.pending_operator == "*":
            self.multiply()
        if self.pending_operator == "/":
            self.division()

    def add(self):
        self.display = float(self.left_operand) + float(self.display)
        self.decimal_check()

    def sub(self):
        self.display = float(self.left_operand) - float(self.display)
        self.decimal_check()

    def multiply(self):
        self.display = float(self.left_operand) * float(self.display)
        self.decimal_check()

    def division(self):
        if self.left_operand == 0 or self.display == 0:
            self.display = 0
        else:
            self.display = float(self.left_operand) / float(self.display)
        self.decimal_check()

    def inverse(self):
        if self.display == '0':
            pass
        else:
            if self.display[0] == '-':
                self.display = self.display[1:]
            else:
                self.display = '-' + self.display

    def decimal_check(self):
        if '.' in str(self.display):
            print(self.get_display())
        else:
            self.display = str(self.display) + '.'
            print(self.get_display())
            self.display = self.display[:-1]

    def clear(self):
        self.left_operand = '0'
        self.pending_operator = ''
        self.display = '0'
        self.start_new_number = True
        self.decimal_flag = False
        self.decimal_check()

    def partial_clear(self):
        self.display = '0'
        self.start_new_number = True
        self.decimal_flag = False
        self.decimal_check()

    def get_display(self):
        if '..' in str(self.display):
            self.display = self.display.replace('..', '.')


        return self.display

    def draw(self):
        window = Tk()
        window.title("The Calculatorium")
        GUI_display = StringVar()
        GUI_display.set(self.display)

        displayLabel = Label(window, textvariable=GUI_display)
        displayLabel.grid(row=0, column=4)
        Button(window, text=" AC  ", command=lambda: self.button_pressed('c')).grid(row=1, column=0)
        Button(window, text=" CE  ", command=lambda: self.button_pressed('ce')).grid(row=1, column=1)
        Button(window, text=" +/- ", command=lambda: self.button_pressed('$')).grid(row=1, column=2)
        Button(window, text="  ÷  ", command=lambda: self.button_pressed('/')).grid(row=2, column=0)
        Button(window, text="  7  ", command=lambda: self.button_pressed('7')).grid(row=2, column=0)
        Button(window, text="  8  ", command=lambda: self.button_pressed('8')).grid(row=2, column=1)
        Button(window, text="  9  ", command=lambda: self.button_pressed('9')).grid(row=2, column=2)
        Button(window, text="  x  ", command=lambda: self.button_pressed('*')).grid(row=2, column=3)
        Button(window, text="  4  ", command=lambda: self.button_pressed('4')).grid(row=3, column=0)
        Button(window, text="  5  ", command=lambda: self.button_pressed('5')).grid(row=3, column=1)
        Button(window, text="  6  ", command=lambda: self.button_pressed('6')).grid(row=3, column=2)
        Button(window, text="  -  ", command=lambda: self.button_pressed('-')).grid(row=3, column=3)
        Button(window, text="  1  ", command=lambda: self.button_pressed('1')).grid(row=4, column=0)
        Button(window, text="  2  ", command=lambda: self.button_pressed('2')).grid(row=4, column=1)
        Button(window, text="  3  ", command=lambda: self.button_pressed('3')).grid(row=4, column=2)
        Button(window, text="  +  ", command=lambda: self.button_pressed('+')).grid(row=4, column=3)
        Button(window, text="  0  ", command=lambda: self.button_pressed('0')).grid(row=5, column=0, rowspan=2)
        Button(window, text="  .  ", command=lambda: self.button_pressed('.')).grid(row=5, column=2)
        Button(window, text="  =  ", command=lambda: self.button_pressed('=')).grid(row=5, column=3)

        window.mainloop()




if __name__ == "__main__":
    test = CalculatorGuts()
    test.draw()
