'''
Jacob Knecht
Prof. Ordonez
CPTR-215
11/02/17
Duration Lab 09
'''


class Duration:
    def __init__(self, *args):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.all_zero = False
        if len(args) == 0:
            print('Please enter a time argument.')
        elif len(args) == 3 and type(args[0]) == int:
            self.seconds = int(args[2])
            self.minutes = int(args[1])
            self.hours = int(args[0])
            print('Track1')
        elif len(args) == 1:
            if type(args[0]) == int:
                print('Track2')
                self.seconds = int(args[0])
                if self.seconds > 60:
                    self.minutes = self.seconds // 60
                    self.seconds = self.seconds % 60
                    if self.minutes > 60:
                        self.hours = self.minutes // 60
                        self.minutes = self.minutes % 60
                elif self.seconds < -60:
                    self.minutes = -self.seconds // 60
                    self.minutes = -self.minutes
                    self.seconds = -self.seconds % 60
                    if self.minutes < -60:
                        self.hours = -self.minutes // 60
                        self.hours = -self.hours
                        self.minutes = -self.minutes % 60
                elif self.seconds == 0:
                    self.seconds, self.minutes, self.hours = str(self.seconds).zfill(2), str(self.minutes).zfill(2), str(self.hours).zfill(2)
                    self.all_zero = True
            elif type(args[0]) == str:
                if ':' in args[0]:
                    print('Track3')
                    time_list = args[0].split(':')
                    if len(time_list) == 2:
                        print('Track3.1')
                        self.hours = int(time_list[0])
                        self.minutes = int(time_list[1])
                    elif len(time_list) == 3:
                        print('Track3.2')
                        self.hours = int(time_list[0])
                        self.minutes = int(time_list[1])
                        self.seconds = int(time_list[2])
                    else:
                        print('Track3.3')
                        self.seconds = int(args[0])
                elif len(args[0]) >= 6:
                    print('Track4')
                    hours_list = args[0].split('h')
                    print(hours_list)
                    minutes_list = hours_list[1].split('m')
                    seconds_list = minutes_list[1].split('s')
                    self.hours = hours_list[0]
                    # print(self.hours)
                    self.minutes = minutes_list[0]
                    # print(self.minutes)
                    self.seconds = seconds_list[0]
                    # print(self.seconds)
                else:
                    if 'h' in args[0]:
                        self.hours = int(args[0][:-1])
                    if 'm' in args[0]:
                        self.minutes = int(args[0][:-1])
                    if 's' in args[0]:
                        self.seconds = int(args[0][:-1])

    def __repr__(self):
        # return "Duration(%s, %s, %s)" % (str(self.hours), str(self.minutes), str(self.seconds))
        if self.seconds == 0 or self.all_zero == True:
            return "Duration(%s:%s)" % (str(self.hours), str(self.minutes))
        else:
            return "Duration(%s:%s:%s)" % (str(self.hours), str(self.minutes), str(self.seconds))

    def __str__(self):
        if self.seconds == 0 or self.all_zero == True:
            return "Duration(%s:%s)" % (str(self.hours), str(self.minutes))
        else:
            return "Duration(%s:%s:%s)" % (str(self.hours), str(self.minutes), str(self.seconds))

    def __mul__(self, other):
        '''
        >>> str(Duration(45) * (2 * 60))
        'Duration(1:30)'

        '''
        return Duration(self.convert_to_seconds() * int(other))

    def __sub__(self, other):
        return Duration(self.convert_to_seconds() - int(other.convert_to_seconds()))

    def __add__(self, other):
        return Duration(self.convert_to_seconds() + int(other.convert_to_seconds()))

    def convert_to_seconds(self):
        return int(self.hours) * 3600 + int(self.minutes) * 60 + int(self.seconds)



if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(Duration('8h23m47s') * 60)
    min90 = Duration("1:30")
    sec45 = Duration("0h0m45s")
    print(min90 - sec45)
    print(sec45 - min90)
    print(Duration('1m'))
    print(sec45 + Duration('1m'))
    print(sec45 - sec45)