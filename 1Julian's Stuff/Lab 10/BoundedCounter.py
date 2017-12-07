'''
Julian Ancion
Prof. Ordonez
CPTR-215
11/08/2017
Bounded Counter
Contains four different classes involving different coutners
'''
class BoundedCounter:
    '''
    The main class, written by Prof. Ordonez.
    '''
    def __init__(self, lower_bound=0, upper_bound=9, neighbor=None):
        '''
        Initializes the counter class
        :param lower_bound: the bottom of the counter, when it reaches the upper_bound it resets to this point
        :param upper_bound: the top of the counter, when it reaches this point the counter resets to the lower_bound
        :param neighbor: (Not needed) when this is used, when the upper_bound is reached it will increment the neighbor
                            by one
        '''
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.current_value = lower_bound
        self.neighbor = neighbor

    def __repr__(self):
        return "%d [%d,%d] -> %r" % \
               (self.current_value, self.lower_bound, self.upper_bound, self.neighbor)

    def increment(self):
        '''
        Increments the counters current value by one
        :return: nothing
        >>> var = BoundedCounter(1, 10)
        >>> var.increment()
        >>> print(var.current_value)
        2
        >>> var = BoundedCounter(1, 4)
        >>> var.increment()
        >>> var.increment()
        >>> var.increment()
        >>> var.increment()
        >>> print(var.current_value)
        1
        '''
        self.current_value += 1
        if self.current_value > self.upper_bound:
            self.current_value = self.lower_bound
            if self.neighbor is not None:
                self.neighbor.increment()

    def decrement(self):
        '''
        decrements the current value by one
        :return: nothing
        >>> var = BoundedCounter(1, 10)
        >>> var.decrement()
        >>> print(var.current_value)
        10
        >>> var = BoundedCounter(1, 4)
        >>> var.decrement()
        >>> var.decrement()
        >>> var.decrement()
        >>> var.decrement()
        >>> print(var.current_value)
        1
        '''
        self.current_value -= 1
        if self.current_value < self.lower_bound:
            self.current_value = self.upper_bound
            if self.neighbor is not None:
                self.neighbor.decrement()

    def get_value(self):
        '''
        returns the value of the bounded counter
        :return: current value
        >>> var = BoundedCounter(1, 10)
        >>> print(var.get_value())
        1
        >>> var = BoundedCounter(1, 10)
        >>> var.decrement()
        >>> print(var.get_value())
        10
        '''
        return self.current_value

    def __str__(self):
        '''
        formats the string output
        :return: combination of neighbor and current value
        '''
        answer = ""
        if self.neighbor is not None:
            answer = str(self.neighbor)
        answer += str(self.current_value)
        return answer
class Odometer:
    '''
    Odometer class to keep track of miles from the hundred thousands down to the tenths
    '''
    def __init__(self):
        '''

        '''
        self.hundred_thousands = BoundedCounter()
        self.ten_thousnads = BoundedCounter(0, 9,self.hundred_thousands)
        self.thousands = BoundedCounter(0, 9, self.ten_thousnads)
        self.hundreds = BoundedCounter(0, 9, self.thousands)
        self.tens = BoundedCounter(0, 9, self.hundreds)
        self.ones = BoundedCounter(0, 9, self.tens)
        self.tenths = BoundedCounter(0, 9, self.ones)

    def __str__(self):
        '''
        formats the string output of the odometer class
        :return: formatted string containing the number of miles
        '''
        return "%d%d%d%d%d%d:%d" % (self.hundred_thousands.current_value, self.ten_thousnads.current_value,
                                     self.thousands.current_value, self.hundreds.current_value,
                                     self.tens.current_value, self.ones.current_value, self.tenths.current_value)

    def advance_tenth(self, *args):
        '''
        advances the tenth of a mile counter
        :param args: (optional) if used, adds that many tenths of a mile to the odometer, else adds one to the counter
        :return: nothing
        >>> var = Odometer()
        >>> var.advance_tenth()
        >>> print(var)
        000000:1
        >>> var.advance_tenth(10)
        >>> print(var)
        000001:1
        '''
        if len(args) == 0:
            self.tenths.increment()
        else:
            for i in range(args[0]):
                self.tenths.increment()

    def advance_mile(self, *miles):
        '''
        advances the mile counter of the odometer
        :param miles: (optional) if used, adds that many miles to the odometer, else adds one to the counter
        :return: nothing
        >>> var = Odometer()
        >>> var.advance_mile()
        >>> print(var)
        000001:0
        >>> var.advance_mile(10)
        >>> print(var)
        000011:0
        '''
        if len(miles) == 1:
            for i in range(0, miles[0]):
                self.ones.increment()
        else:
            self.ones.increment()

class DigitalClock:
    '''
    digital clock class
    '''
    def __init__(self):
        '''
        initializes the digital clock
        '''
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
        '''
        Advances the clock by seconds
        :param args: (option) if included adds the set amount to the number of seconds else advances by one
        :return: nothing
        '''
        if len(args) == 0:
            self.seconds.increment()
        elif len(args) == 1:
            for i in range(args[0]):
                self.seconds.increment()

class BaseballCounter:
    def __init__(self):
        '''
        initializes the BaseballCounter class with default values
        '''
        self.inning = BoundedCounter(1, 9)
        self.half = BoundedCounter(1, 2, self.inning)
        self.outs = BoundedCounter(0, 2, self.half)
        self.ball = BoundedCounter(0, 3)
        self.strike = BoundedCounter(0, 2, self.outs)
        self.home_score = 0
        self.away_score = 0
        self.top_bot = 'top'

    def __str__(self):
        '''
        formats the output for strings
        :return: formatted string
        '''
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

    def hit(self):
        '''
        resets the ball and strike counters to represent new batter
        :return: nothing
        >>> var = BaseballCounter()
        >>> var.strikeup()
        >>> print(var.strike.current_value)
        1
        >>> var.hit()
        >>> print(var.strike.current_value)
        0
        >>> var = BaseballCounter()
        >>> var.ballup()
        >>> print(var.ball.current_value)
        1
        >>> var.hit()
        >>> print(var.ball.current_value)
        0
        '''
        self.ball.current_value = 0
        self.strike.current_value = 0

    def strikeup(self):
        '''
        inccrements the strike count of the current batter
        :return: nothing
        >>> var = BaseballCounter()
        >>> var.strikeup()
        >>> print(var.strike.current_value)
        1
        >>> var.strikeup()
        >>> var.strikeup()
        >>> print(var.strike.current_value)
        0
        '''
        self.strike.increment()

    def ballup(self):
        '''
        increments the ball count for the current player
        :return: nothing
        >>> var = BaseballCounter()
        >>> var.ballup()
        >>> print(var.ball.current_value)
        1
        >>> var.ballup()
        >>> var.ballup()
        >>> var.ballup()
        >>> print(var.ball.current_value)
        0
        '''
        self.ball.increment()

    def runup(self):
        '''
        increments the score of the current team, home bats in the top away bats in the bottom
        :return: nothing
        >>> var = BaseballCounter()
        >>> var.runup()
        >>> print(var.home_score)
        1
        >>> var.change_sides()
        >>> var.runup()
        >>> print(var.away_score)
        1
        '''
        if self.half.current_value == 1:
            self.home_score += 1
        else:
            self.away_score += 1

    def change_sides(self):
        '''
        changes what the current half is top/1 or bottom/2
        :return: nothing
        >>> var = BaseballCounter()
        >>> print(var.half.current_value)
        1
        >>> var.change_sides()
        >>> print(var.half.current_value)
        2
        >>> var.change_sides()
        >>> print(var.half.current_value)
        1
        '''
        self.outs = BoundedCounter(0, 2, self.half)
        self.ball = BoundedCounter(0, 3)
        self.strike = BoundedCounter(0, 2, self.outs)
        self.half.increment()

    def get_balls(self):
        '''
        returns the value of the current ball count
        :return: ball count
        >>> var = BaseballCounter()
        >>> print(var.get_balls())
        0 balls
        >>> var = BaseballCounter()
        >>> var.ballup()
        >>> print(var.get_balls())
        1 balls
        '''
        return "%d balls" % self.ball.current_value

    def get_strikes(self):
        '''
        returns the value of current strikes
        :return: formatted string of number of strikes
        >>> var = BaseballCounter()
        >>> print(var.get_strikes())
        0 strikes
        >>> var = BaseballCounter()
        >>> var.strikeup()
        >>> print(var.get_strikes())
        1 strikes
        '''
        return "%d strikes" % self.strike.current_value

    def get_outs(self):
        '''
        returns the current number of outs
        :return: returns number of outs in formatted string
        >>> var = BaseballCounter()
        >>> print(var.get_outs())
        0 outs
        >>> var = BaseballCounter()
        >>> var.strikeup()
        >>> var.strikeup()
        >>> var.strikeup()
        >>> print(var.get_outs())
        1 outs
        '''
        return "%d outs" % self.outs.current_value

    def get_half(self):
        '''
        :return: what half of the inning it is currently
        >>> var = BaseballCounter()
        >>> var.get_half()
        'Top of the inning'
        >>> var.change_sides()
        >>> var.get_half()
        'Bottom of the inning'
        '''
        if self.half.current_value == 1:
            return "Top of the inning"
        else:
            return "Bottom of the inning"

    def get_inning(self):
        '''

        :return: current inning in formatted string
        >>> var = BaseballCounter()
        >>> var.get_inning()
        '1st inning'
        >>> var.change_sides()
        >>> var.change_sides()
        >>> var.get_inning()
        '2nd inning'

        '''
        if self.inning.current_value == 1:
            string = 'st'
        elif self.inning.current_value == 2:
            string = 'nd'
        elif self.inning.current_value == 3:
            string = 'rd'
        else:
            string = 'th'
        return "%d%s inning" % (self.inning.current_value, string)

    def get_score(self):
        '''
        :return: returns a tuple of home/away scores
        >>> var = BaseballCounter()
        >>> var.get_score()
        (0, 0)
        >>> var.runup()
        >>> var.runup()
        >>> var.runup()
        >>> var.get_score()
        (3, 0)
        '''
        return self.home_score, self.away_score

    def reset_all(self):
        '''
        reinitializes the counters with the init function
        :return:nothing
        >>> var = BaseballCounter()
        >>> var.reset_all()
        >>> print(var)
        0 balls, 0 strikes, 0 out, top of the 1st inning, score: 0:0
        >>> var.strikeup()
        >>> var.reset_all()
        >>> print(var)
        0 balls, 0 strikes, 0 out, top of the 1st inning, score: 0:0
        '''
        self.__init__()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    miles = Odometer()

    miles.advance_tenth(12)
    miles.advance_mile(999998)
    print(miles)

    time = DigitalClock()
    print(time)
    time.tick()
    print(time)

    score = BaseballCounter()
    print(score)
    score.strikeup()
    print(score)
    for i in range(11):
        score.strikeup()

    print(score)

