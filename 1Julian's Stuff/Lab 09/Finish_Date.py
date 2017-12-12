'''
Julian Ancion
Prof. Ordonez
CPTR-215
10/26/2017
Finish Date Lab
'''

class Date:
    DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, *args):
        '''
        Initializes the class
        :param args:
        '''
        if type(args[0]) == str:
            self.year, self.month, self.day = map(int, args[0].split('-'))
        else:
            self.year, self.month, self.day = args

    def __repr__(self):
        """Returns a string that, when evaluated, creates an identical object.
        >>> Date("2109-8-7")
        Date(2109, 8, 7)
        >>> Date(2017, 10, 26)
        Date(2017, 10, 26)
        >>> Date(1991, 7, 6)
        Date(1991, 7, 6)
        """
        return "Date(%d, %d, %d)" % (self.year, self.month, self.day)

    def __str__(self):
        """Returns a human-readable date string in the form yyyy-mm-dd.
        >>> str(Date("4321-12-31"))
        '4321-12-31'
        >>> str(Date(2017, 10, 26))
        '2017-10-26'
        >>> str(Date(2000, 2, 9))
        '2000-02-09'
        """
        return "%04d-%02d-%02d" % (self.year, self.month, self.day)

    def __sub__(self, other):  # other may be a Date or an int
        '''
        Calls either sub_date or previous day based on input
        :param other:
        :return:
        '''
        if type(other) == type(1):
            new_date = self
            for i in range(other):
                new_date = new_date.previous_day()
            return new_date
        else:
            days_out = Date.sub_date(self, other)
            return days_out

    def sub_date(self, lesser_date):
        '''

        :param lesser_date:
        :return:
        '''
        num = 0
        new_date = self
        while self != lesser_date:
            num += 1
            new_date = new_date.previous_day()

        return num

    def previous_day(self):
        '''
        Returns the Previous date
        :return: Date(year, month, day)
        >>> Date(1991, 7, 6).previous_day()
        Date(1991, 7, 5)
        >>> Date(2000, 3, 1).previous_day()
        Date(2000, 2, 29)
        >>> Date(1994, 3, 10).previous_day()
        Date(1994, 3, 9)
        >>> #Date(2000, 1, 1).previous_day()
        #Date(1999, 12, 31)
        '''
        new_year, new_month, new_day = self.year, self.month, self.day - 1
        month = Date.DAYS_IN_MONTH[self.month - 1]
        if Date(self.year, self.month, self.day).is_in_leap_year() and self.month == 3:
            month = 29
        if new_day == 0:
            new_month -= 1
            new_day = month
        if new_month == 0:
            new_year -= 1
            new_month = 12
        return Date(new_year, new_month, new_day)



    def day_of_week(self):
        '''
        Returns the Day of the week
        :return: String containing the day of the week
        >>> Date(1991, 7, 6).day_of_week()
        'Sabbath'
        >>> Date(2004, 3, 9).day_of_week()
        'Tuesday'
        >>> Date(1, 1, 1).day_of_week()
        'Sabbath'
        '''
        day_dict = {

            2: 'Monday',
            3: 'Tuesday',
            4: 'Wednesday',
            5: 'Thursday',
            6: 'Friday',
            0: 'Sabbath',
            1: 'Sunday',
        }
        Y = int(self.year)
        q = int(self.day)
        m = int(self.month)
        if (self.month == '01') or (self.month == '02'):
            Y -= 1
            m += 12
        h = (q + 13 * (m + 1) / 5 + Y + Y // 4 - Y // 100 + Y // 400) % 7
        return day_dict[int(h)]

    def is_in_leap_year(self):
        """Determines whether this date falls within a leap year.

        >>> Date(2000, 5, 27).is_in_leap_year()
        True
        >>> Date(1900, 2, 5).is_in_leap_year()
        False
        >>> Date(2016, 2, 29).is_in_leap_year()
        True
        >>> Date(2017, 10, 26).is_in_leap_year()
        False
        """
        return ((self.year % 4 == 0) and (self.year % 100 != 0)) or (self.year % 400 == 0)

    def __add__(self, offset):
        '''
        calles the next day function until the loop finishes then returns the date
        :param offset:
        :return: Date
        '''
        new_date = self
        for i in range(offset):
            new_date = new_date.next_day()
        return new_date

    def next_day(self):
        '''
        :return:

        >>> Date(2017, 10, 26).next_day()
        Date(2017, 10, 27)
        >>> Date(2017, 10, 31).next_day()
        Date(2017, 11, 1)
        >>> Date(2017, 12, 31).next_day()
        Date(2018, 1, 1)
        >>> Date(2000, 2, 28).next_day()
        Date(2000, 2, 29)
        >>> Date(1999, 2, 28).next_day()
        Date(1999, 3, 1)

        '''

        new_year, new_month, new_day = self.year, self.month, self.day + 1
        month = Date.DAYS_IN_MONTH[self.month]
        if Date(new_year, new_month, new_day).is_in_leap_year() and new_month == 2:
            month = 29
        if new_day > month:
            new_month += 1
            new_day = 1
        if new_month > 12:
            new_year += 1
            new_month = 1
        return Date(new_year, new_month, new_day)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    birthdate = Date(input("Enter a date: "))
    today = Date(2016, 3, 1)
    #print("Today you are %d days old!" % (today - birthdate))
    print("You were born on a %s." % birthdate.day_of_week())
    if birthdate.is_in_leap_year():
        print("You were born in a leap year")
    else:
        print("You were born in a non-leap year")
    print("Yesterday's date was %s." % (birthdate - 1))
    print("Tomorrow's date is %s." % (birthdate + 1))
