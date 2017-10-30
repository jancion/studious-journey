class Date:
    DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, *args):
        if type(args[0]) == str:
            self.year, self.month, self.day = map(int, args[0].split('-'))
        else:
            self.year, self.month, self.day = args

    def __repr__(self):
        return "Date(%d, %d, %d)" % (self.year, self.month, self.day)

    def __str__(self):
        return "%04d-%02d-%02d" % (self.year, self.month, self.day)

    def __sub__(self, other):  # other may be a Date or an int
        if type(other) == 'int':
            self.sub_int(other)
        else:
            self.convert_date(other)

    def convert_date(self, offset):
        offset = str(offset)
        sub_year = int(offset[0])
        sub_month = int(offset[1])
        sub_day = int(offset[2])
        self.sub_date(sub_year, sub_month, sub_day)

    def sub_date(self, year, month, day):
        import math
        new_year = self.year - year
        new_month = self.month - month
        new_day = self.day - day
        total = math.floor(new_year * 365.25) + new_day
        for x in range(new_month):
            total += self.DAYS_IN_MONTH[x]
        return total

    def sub_int(self, offset):
        new_date = self
        for i in range(offset):
            new_date = new_date.yesterday()
        return new_date

    def yesterday(self):
        new_year, new_month, new_day = self.year, self.month, self.day - 1
        if new_day == 0:
            new_month -= 1
            new_day = Date.DAYS_IN_MONTH[new_month]
        if new_month == 0:
            new_year -= 1
            new_month = 12
        return Date(new_year, new_month, new_day)

    def day_of_week(self):
        weekday = ('Sabbath', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
        year = int(self.year)
        month = int(self.month)
        day = int(self.day)
        if month == 1:
            year = year - 1
            month = 13
        elif month == 2:
            year = year - 1
            month = 14

        currentDay = (day + 13 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400) % 7
        return weekday[currentDay]

    def is_in_leap_year(self):
        return ((self.year % 4 == 0) and (self.year % 100 != 0)) or (self.year % 400 == 0)

    def __add__(self, offset):
        new_date = self
        for i in range(offset):
            new_date = new_date.next_day()
        return new_date

    def next_day(self):
        new_year, new_month, new_day = self.year, self.month, self.day + 1
        if new_day > Date.DAYS_IN_MONTH[self.month]:
            new_month += 1
            new_day = 1
        if new_month > 12:
            new_year += 1
            new_month = 1
        return Date(new_year, new_month, new_day)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    birthdate = Date(input("Enter your date of birth in yyyy-mm-dd format: "))
    today = Date(2017, 10, 25)
    print("Today you are %d days old!" % (today - birthdate))
    print("You were born on a %s." % birthdate.day_of_week())
    if birthdate.is_in_leap_year():
        print("You were born in a leap year")
    else:
        print("You were born in a non-leap year")
    print("Yesterday's date was %s." % (today - 1))
    print("Tomorrow's date is %s." % (today + 1))