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
        self.zero = False
        if len(args) == 0:
            print('Please enter arguments')
        elif len(args) == 1 and type(args[0]) == int:
            self.seconds = args[0]
            self.minutes = 0
            self.hours = 0
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
        if int(self.seconds) >= 60:
            self.minutes = self.minutes + self.seconds // 60
            self.seconds = self.seconds % 60
        if int(self.minutes) >= 60:
            self.hours = self.hours + self.minutes // 60
            self.minutes = self.minutes % 60
        if int(self.seconds) < -60:
            self.minutes = -self.seconds // 60
            self.minutes = -self.minutes
            self.seconds = -self.seconds % 60
            if self.minutes < -60:
                self.hours = -self.minutes // 60
                self.hours = -self.hours
                self.minutes = -self.minutes % 60
        if self.seconds == 0:
            self.seconds, self.minutes, self.hours = str(self.seconds).zfill(2), str(self.minutes).zfill(2), str(self.hours).zfill(2)
            self.zero = True
    def __repr__(self):
        if self.zero == True or self.seconds == 0:
            return "Duration(%s:%s)" % (str(self.hours), str(self.minutes))
        else:
            return "Duration(%s:%s:%s)" % (str(self.hours), str(self.minutes), str(self.seconds))

    def __str__(self):
        if self.zero == True or self.seconds == 0:
            return "Duration(%s:%s)" % (str(self.hours), str(self.minutes))
        else:
            return "Duration(%s:%s:%s)" % (str(self.hours), str(self.minutes), str(self.seconds))

    def __add__(self, other):
        self.seconds += other.seconds
        if self.seconds >= 60:
            self.minutes = self.minutes + self.seconds // 60
            self.seconds = self.seconds % 60
        self.minutes += other.minutes
        if int(self.minutes) >= 60:
            self.hours = self.hours + self.minutes // 60
            self.minutes = self.minutes % 60
        self.hours += other.hours
        return Duration(self.hours, self.minutes, self.seconds)

    def __sub__(self, other):
        return Duration(self.seconds_convert() - int(other.seconds_convert()))

    def __eq__(self, other):
        true_count = 0
        if self.hours == other.hours:
            true_count += 1
        if self.minutes == other.minutes:
            true_count += 1
        if self.seconds == other.seconds:
            true_count += 1
        if true_count == 3:
            return True
        else:
            return False

    def __gt__(self, other):
        true_count = 0
        if int(self.hours) > int(other.hours):
            true_count += 1
        if int(self.minutes) > int(other.minutes):
            true_count += 1
        if int(self.seconds) > int(other.seconds):
            true_count += 1
        if true_count == 3:
            return True
        else:
            return False

    def __ge__(self, other):
        true_count = 0
        if int(self.hours) >= int(other.hours):
            true_count += 1
        if int(self.minutes) >= int(other.minutes):
            true_count += 1
        if int(self.seconds) >= int(other.seconds):
            true_count += 1
        if true_count == 3:
            return True
        else:
            return False

    def __lt__(self, other):
        true_count = 0
        if int(self.hours) < int(other.hours):
            true_count += 1
        if int(self.minutes) < int(other.minutes):
            true_count += 1
        if int(self.seconds) < int(other.seconds):
            true_count += 1
        if true_count == 3:
            return True
        else:
            return False

    def __le__(self, other):
        true_count = 0
        if self.hours <= other.hours:
            true_count += 1
        if self.minutes <= other.minutes:
            true_count += 1
        if self.seconds <= other.seconds:
            true_count += 1
        if true_count == 3:
            return True
        else:
            return False

    def seconds_convert(self):
        return int(self.hours) * 3600 + int(self.minutes) * 60 + int(self.seconds)


dur_almost_1_day = Duration(23, 59, 59)
dur_90_min = Duration("1:30")
dur_45_sec = Duration("0h0m45s")
dur_1_min = Duration(60)
dur_60_sec = Duration(0, 0, 60)

if dur_1_min == dur_60_sec:
    print(True)
if dur_1_min > dur_45_sec:
    print(False)
print(dur_almost_1_day)
print(dur_90_min)
print(dur_45_sec)
print(dur_1_min)
