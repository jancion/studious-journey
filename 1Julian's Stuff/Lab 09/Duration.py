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
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        if len(args) == 0:
            print('Please enter arguments')
        elif len(args) == 1 and type(args[0]) == int:
            self.seconds = args[0]
            self.minutes = 0
            self.hours = 0
            if self.seconds > 60:
                self.minutes = self.seconds // 60
                self.seconds = self.seconds % 60
                if self.minutes > 60:
                    self.hours = self.minutes // 60
                    self.minutes = self.minutes % 60
        elif len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif len(args) == 1 and type(args[0]) == str:
            if ':' in args[0]:
                data = args[0].split(':')
                if len(data) == 2:
                    self.minutes = data[0]
                    self.seconds = data[1]
                elif len(data) == 3:
                    self.hours = data[0]
                    self.minutes = data[1]
                    self.seconds = data[2]
                else:
                    self.seconds = args[0]
            else:
                data1 = args[0].split('h')
                data2 = data1[1].split('m')
                self.hours = data1[0]
                self.minutes = data2[0]
                self.seconds = data2[1].strip('s')

        else:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0

    def __repr__(self):
        return "Duration(%s:%s:%s)" % (self.hours, self.minutes, self.seconds)

    def __str__(self):
        return "Duration(%s:%s:%s)" % (self.hours, self.minutes, self.seconds)


test = Duration(60001)
test2 = Duration(1, 2, 3)
test3 = Duration('1:2:3')
test4 = Duration('3h2m1s')
print(test)
print(test2)
print(test3)
print(test4)
