'''
Julian Ancion
Prof. Ordonez
CPTR-215
11/08/2017
Bounded Counter
'''
class BoundedCounter:
    def __init__(self, lower_bound=0, upper_bound=9, neighbor=None):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.current_value = lower_bound
        self.neighbor = neighbor

    def __repr__(self):
        return "%d [%d,%d] -> %r" % \
               (self.current_value, self.lower_bound, self.upper_bound, self.neighbor)

    def increment(self):
        self.current_value += 1
        if self.current_value > self.upper_bound:
            self.current_value = self.lower_bound
            if self.neighbor is not None:
                self.neighbor.increment()

    def decrement(self):
        self.current_value -= 1
        if self.current_value < self.lower_bound:
            self.current_value = self.upper_bound
            if self.neighbor is not None:
                self.neighbor.decrement()

    def get_value(self):
        return self.current_value

    def __str__(self):
        answer = ""
        if self.neighbor is not None:
            answer = str(self.neighbor)
        answer += str(self.current_value)
        return answer
class Odometer:
    def __init__(self):
        self.hundred_thousands = BoundedCounter()
        self.ten_thousnads = BoundedCounter(0, 9,self.hundred_thousands)
        self.thousands = BoundedCounter(0, 9, self.ten_thousnads)
        self.hundreds = BoundedCounter(0, 9, self.thousands)
        self.tens = BoundedCounter(0, 9, self.hundreds)
        self.ones = BoundedCounter(0, 9, self.tens)
        self.tenths = BoundedCounter(0, 9, self.ones)

    def __str__(self):
        return "%d%d%d%d%d%d:%d:" % (self.hundred_thousands.current_value, self.ten_thousnads.current_value,
                                     self.thousands.current_value, self.hundreds.current_value,
                                     self.tens.current_value, self.ones.current_value, self.tenths.current_value)

    def advance_tenth(self):
        self.tenths.increment()

    def advance_mile(self, miles):
        for i in range(0, miles):
            self.ones.increment()

class DigitalClock:
    def __init__(self):
        self.AMPM = BoundedCounter(0, 1)
        self.hours = BoundedCounter(1, 12, self.AMPM)
        self.minutes = BoundedCounter(0, 59, self.hours)
        self.seconds = BoundedCounter(0, 59, self.minutes)
        self.ampm = 'am'

    def __str__(self):
        if self.AMPM.current_value == 0:
            self.ampm = 'am'
        else:
            self.ampm = 'pm'
        return '%02d:%02d %s' % (self.hours.current_value, self.minutes.current_value, self.ampm)

    def tick(self, *args):
        if len(args) == 0:
            self.seconds.increment()
        elif len(args) == 1:
            for i in range(args[0]):
                self.seconds.increment()

class BaseballCounter:
    def __init__(self):
        self.inning = BoundedCounter(0, 9)
        self.half = BoundedCounter(1, 2, self.inning)
        self.outs = BoundedCounter(0, 3, self.half)
        self.ball = BoundedCounter(0, 4)
        self.strike = BoundedCounter(0, 3, self.outs)
        self.home_score = 0
        self.away_score = 0
        self.top_bot = 'top'

    def __str__(self):
        if self.half.current_value == 1:
            self.top_bot = 'top'
        else:
            self.top_bot = 'bottom'
        if self.inning.current_value == 1:
            string = 'st'
        elif self.inning.current_value == 2:
            string = 'nd'
        elif self.inning.current_value == 3:
            string = 'rd'
        else:
            string = 'th'

        return "%d balls, %d strikes, %d out, %s of the %d%s inning, score: %s:%s" % (self.ball.current_value,
                                                                                      self.strike.current_value,
                                                                                      self.outs.current_value,
                                                                                      self.top_bot,
                                                                                      self.inning.current_value,
                                                                                      string, self.home_score,
                                                                                      self.away_score)
        def hit():
            pass
        def strikeup():
            pass
        def ballup():
            pass
        def runup():
            pass
        def change_sides():
            pass
        def get_balls():
            pass
        def get_strikes():
            pass
        def get_outs():
            pass
        def get_half():
            pass
        def get_inning():
            pass
        def get_score():
            pass
        def reset_all():
            pass

if __name__ == "__main__":
    pass
    miles = Odometer()
    miles.advance_tenth()
    miles.advance_mile(200)
    print(miles)

    time = DigitalClock()
    print(time)
    time.tick()
    print(time)

    score = BaseballCounter()
    print(score)

    ##    hundreds = BoundedCounter()
    ##    tens = BoundedCounter(0, 9, hundreds)
    ##    ones = BoundedCounter(0, 9, tens)
    ##    tenths = BoundedCounter(0, 9, ones)
    # clock

    # ampm = BoundedCounter(0, 1)
    # hours = BoundedCounter(1, 12, ampm)
    # minutes = BoundedCounter(0, 59, hours)

    # print(ampm)
    # print(hours)
    # print(minutes)
