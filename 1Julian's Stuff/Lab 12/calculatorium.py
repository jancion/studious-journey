'''
Julian Ancion
Prof. Ordonez
CPTR-215
Calculator
'''
from tkinter import *


class CalculatorGuts:
    '''
    Core framework of the calculator.
    '''

    def __init__(self, *args):
        '''
        Initializes all the variables needed for the calculator to function
        '''
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
        '''
        Tells the console what to print out when the function is called.
        '''
        return "%s" % (self.display)

    def button_pressed(self, button):
        '''
        Detects when a button is pressed and determines whether it is a number or operator
        and redirects it to the appropriate function.
        '''
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
        '''
        If a number is pressed this function is called and adds that number to The
        display and detects it is a number after an operator.
        '''
        if button == '.':
            if '.' in self.display:
                pass
            else:
                self.decimal_flag = True
                self.display += '.'
        if self.start_new_number is True:
            self.display = button
            self.start_new_number = False
        else:
            self.display += button
        self.decimal_check()

    def operator_pressed(self, button):
        '''
        If an operator is pressed then this function determines if it is an equals
        then calls the evaluate function.
        '''
        if self.start_new_number is True:
            if button == '=':
                self.decimal_check()
            else:

                self.pending_operator = button
        else:
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
        '''
        when called it checks the operator and runs the appropriate function.
        '''
        if self.pending_operator == "+":
            self.add()
        if self.pending_operator == "-":
            self.sub()
        if self.pending_operator == "*":
            self.multiply()
        if self.pending_operator == "/":
            self.division()

    def add(self):
        '''
        runs the addition portion of the Calculator.
        '''
        self.display = float(self.left_operand) + float(self.display)
        self.decimal_check()

    def sub(self):
        '''
        runs the subtraction portion of the calculator.
        '''
        self.display = float(self.left_operand) - float(self.display)
        self.decimal_check()

    def multiply(self):
        '''
        runs the, you guessed it, multiplication portion of the calculator.
        '''
        self.display = float(self.left_operand) * float(self.display)
        self.decimal_check()

    def division(self):
        '''
        runs the division portion of the calculator.
        '''
        if self.left_operand == 0 or self.display == 0:
            self.display = 0
        else:
            self.display = float(self.left_operand) / float(self.display)
        self.decimal_check()

    def inverse(self):
        '''
        runs the inverse funtion of the calculator, making a number negative.
        '''
        if self.display == '0':
            pass
        else:
            if self.display[0] == '-':
                self.display = self.display[1:]
            else:
                self.display = '-' + self.display

    def decimal_check(self):
        '''
        checks if the decimal exists in the actual nmber rather than just displayed
        on the end.
        '''
        if '.' in str(self.display):
            print(self.get_display())
        else:
            self.display = str(self.display) + '.'
            print(self.get_display())
            self.display = self.display[:-1]

    def clear(self):
        '''
        Clears the entire input field and left operand.
        '''
        self.left_operand = '0'
        self.pending_operator = ''
        self.display = '0'
        self.start_new_number = True
        self.decimal_flag = False
        self.decimal_check()

    def partial_clear(self):
        '''
        Only clears the active input field.
        '''
        self.display = '0'
        self.start_new_number = True
        self.decimal_flag = False
        self.decimal_check()

    def get_display(self):
        '''
        Checks the display and retrieves it
        '''
        if '..' in str(self.display):
            self.display = self.display.replace('..', '.')

        return self.display

    def draw(self):
        '''
        Draws the GUI including buttons and number field.
        '''
        window = Tk()
        window.title("The Calculatorium")
        GUI_display = StringVar()

        GUI_display.set(str(self.display))

        def set_display():
            GUI_display.set(self.display)

        Label(window, textvariable=GUI_display, justify=RIGHT).grid(row=0, column=0, columnspan=4, sticky=E)

        Button(window, text=" AC  ", command=lambda: [self.button_pressed('c'), set_display()]).grid(row=1, column=0)
        Button(window, text=" CE  ", command=lambda: [self.button_pressed('ce'), set_display()]).grid(row=1, column=1)
        Button(window, text=" +/- ", command=lambda: [self.button_pressed('$'), set_display()]).grid(row=1, column=2)
        Button(window, text="  ÷  ", command=lambda: [self.button_pressed('/'), set_display()]).grid(row=2, column=0)
        Button(window, text="  7  ", command=lambda: [self.button_pressed('7'), set_display()]).grid(row=2, column=0)
        Button(window, text="  8  ", command=lambda: [self.button_pressed('8'), set_display()]).grid(row=2, column=1)
        Button(window, text="  9  ", command=lambda: [self.button_pressed('9'), set_display()]).grid(row=2, column=2)
        Button(window, text="  x  ", command=lambda: [self.button_pressed('*'), set_display()]).grid(row=2, column=3)
        Button(window, text="  4  ", command=lambda: [self.button_pressed('4'), set_display()]).grid(row=3, column=0)
        Button(window, text="  5  ", command=lambda: [self.button_pressed('5'), set_display()]).grid(row=3, column=1)
        Button(window, text="  6  ", command=lambda: [self.button_pressed('6'), set_display()]).grid(row=3, column=2)
        Button(window, text="  -  ", command=lambda: [self.button_pressed('-'), set_display()]).grid(row=3, column=3)
        Button(window, text="  1  ", command=lambda: [self.button_pressed('1'), set_display()]).grid(row=4, column=0)
        Button(window, text="  2  ", command=lambda: [self.button_pressed('2'), set_display()]).grid(row=4, column=1)
        Button(window, text="  3  ", command=lambda: [self.button_pressed('3'), set_display()]).grid(row=4, column=2)
        Button(window, text="  +  ", command=lambda: [self.button_pressed('+'), set_display()]).grid(row=4, column=3)
        Button(window, text="  0  ", width=10, command=lambda: [self.button_pressed('0'), set_display()]).grid(row=5, column=0, columnspan=2)
        Button(window, text="  .  ", command=lambda: [self.button_pressed('.'), set_display()]).grid(row=5, column=2)
        Button(window, text="  =  ", command=lambda: [self.button_pressed('='), set_display()]).grid(row=5, column=3)

        window.mainloop()


if __name__ == "__main__":
    test = CalculatorGuts()
    test.draw()
