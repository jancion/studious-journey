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
    >>> calc.
    '''
    def __init__(self, *args):
        self.left_operand = 0
        self.pending_operator = '+'
        self.display = '0.'
        self.start_new_number = True

    def button_pressed(self, button):
        pass

    def get_display(self):
        pass

