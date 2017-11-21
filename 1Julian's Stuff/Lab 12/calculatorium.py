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
        self.num_list = '0123456789'
        self.operator_list = '$+-*/='

    def button_pressed(self, button):
        if button in self.num_list:
            if self.start_new_number is True:
                # Fresh calculator just turned on, replaces '0.' with pressed number
                self.display = button
                self.start_new_number = False
            else:
                # appends pressed button to number
                self.display += button
        elif button in self.operator_list:
            if self.start_new_number is True:
                # if '0.' and fresh number, have it do nothing if = is pressed
                if button == '=':
                    pass
                else:
                    # numbers have already been put in.
                    self.pending_operator = button
            else:
                # after operand is assigned
                self.left_operand = self.display
                self.pending_operator = button
                self.start_new_number = True

        pass

    def buttons_pressed(self, buttons):
        for button in buttons:
            self.button_pressed(button)

    def get_display(self):
        pass
