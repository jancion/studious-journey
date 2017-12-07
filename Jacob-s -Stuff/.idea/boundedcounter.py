'''
Jacob Knecht
Prof. Ordonez
CPTR-215
11/09/17
Bounded Counter Lab 10
'''


class ConnectedCounter:
    def increment(self):
        pass

    def decrement(self):
        pass


class NoCounter(ConnectedCounter):
    def __repr__(self):
        return "NoCounter()"


class BoundedCounter(ConnectedCounter):
    def __init__(self, values=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), neighbor=NoCounter()):
        self.values = values
        self.current_index = 0
        self.neighbor = neighbor

    def __repr__(self):
        return "%s from %s -> %r" % \
               (self.values[self.current_index], self.values, self.neighbor)

    def increment(self):
        self.current_index += 1
        if self.current_index >= len(self.values):
            self.current_index = 0
            self.neighbor.increment()

    def decrement(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.values) - 1
            self.neighbor.decrement()

    def get_value(self):
        return self.values[self.current_index]

    def __str__(self):
        return str(self.get_value())


class Clock:
    def __init__(self):
        self.ampm = BoundedCounter(("am", "pm"))
        self.hours = BoundedCounter((12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), self.ampm)
        self.minutes = BoundedCounter(["%02d" % minute for minute in range(60)], self.hours)

    def __str__(self):
        return "%2s:%s %s" % (self.hours, self.minutes, self.ampm)

    def tick(self):
        self.minutes.increment()

    def advance(self, minutes):
        for i in range(minutes):
            self.minutes.increment()

