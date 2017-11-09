'''
Jacob Knecht
Prof. Ordonez
CPTR-215
11/02/17
Duration Lab 09
'''
class duration:
    def __init__(self, *args):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        if len(args) == 0:
            print('Please enter a time argument.')
        elif len(args) == 3 and type(args[0]) == int:
            self.seconds = args[2]
            self.minutes = args[1]
            self.hours = args[0]
        elif len(args) == 1:
            if type(args[0]) == int:
                self.seconds = args[0]
                if self.seconds > 60:
                    self.minutes = self.seconds // 60
                    self.seconds = self.seconds % 60
                    if self.minutes > 60:
                        self.hours = self.minutes // 60
                        self.minutes = self.minutes % 60
            elif type(args[0]) == str:
                if ':' in args[0]:
                    time_list = args[0].split(':')
                    if len(time_list) == 2:
                        self.minutes = int(time_list[0])
                        self.seconds = int(time_list[1])
                    elif len(time_list) == 3:
                        self.hours = int(time_list[0])
                        self.minutes = int(time_list[1])
                        self.seconds = int(time_list[2])
                    else:
                        self.seconds = args[0]
                else:
                    print('right way')
                    hours_list = args[0].split('h')
                    minutes_list = hours_list[1].split('m')
                    seconds_list = minutes_list[1].split('s')
                    self.hours = hours_list[0][:-1]
                    self.minutes = minutes_list[0][:-1]
                    self.seconds = seconds_list[0][:-1]

    def __repr__(self):
        return "Duration(%d, %d, %d)" % (self.hours, self.minutes, self.seconds)

    def __str__(self):
        return "Duration(%s:%s:%s)" % (self.hours, self.minutes, self.seconds)

duration('8h23m47s')
