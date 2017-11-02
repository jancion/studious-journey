'''
Julian Ancion
Prof. Ordonez
CPTR-215
11/02/17
Duration Lab 09
'''


class Duration:
    def __init__(self, *args):
        '''
        Initializes the duration class
        '''
        if len(args) == 0:
            print('Please enter arguments')
        elif len(args) == 1 and type(args[0]) == int:
            self.seconds = args[0]
            self.minutes = 0
            self.days = 0
            if self.seconds > 60:
                self.minutes = self.seconds // 60
                self.seconds = self.seconds % 60
                if self.minutes > 60:
                    self.days = self.minutes // 60
                    self.minutes = self.minutes % 60
        elif len(args) == 3:
            self.days = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif len()
        else:
            self.seconds = 0
            self.minutes = 0
            self.days = 0

    def __repr__(self):
        return "Duration(%d:%d:%d)" % (self.days, self.minutes, self.seconds)

    def __str__(self):
        return "Duration(%d:%d:%d)" % (self.days, self.minutes, self.seconds)


test = Duration(6001)
test2 = Duration(1, 2, 3)
print(test2)

