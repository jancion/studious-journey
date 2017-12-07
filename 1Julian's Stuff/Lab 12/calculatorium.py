import math
from tkinter import *


class CalculatorGuts:
    '''
    >>> calc = CalculatorGuts()
    >>> calc.get_display()
    '0.'
    >>> calc.button_pressed('3')
    >>> calc.get_display()
    '3.'
    >>> calc.buttons_pressed('2 + 3 - 8 C 4 =')
    >>> calc.get_display()
    '31.'
    '''

    def __init__(self, *args):
        self.left_operand = '0'
        self.pending_operator = ''
        self.display = '0.'
        self.start_new_number = True
        self.decimal_flag = False
        self.num_list = '0123456789.'
        self.operator_list = '+-*/='
        self.inverse_list = '$'
        self.clear_list = 'c'

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
        if '.' in self.display:
            print(self.get_display())
        else:
            self.display += '.'
            print(self.get_display())
            self.display = self.display[:-1]


    def clear(self):
        self.left_operand = '0'
        self.pending_operator = ''
        self.display = '0.'
        self.start_new_number = True
        self.decimal_flag = False
        self.decimal_check()

    def get_display(self):
        return self.display


calc = CalculatorGuts()
calc.button_pressed('6')
calc.button_pressed('8')
calc.button_pressed('.')
calc.button_pressed('9')
