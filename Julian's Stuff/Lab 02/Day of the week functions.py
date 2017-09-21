'''
Julian Ancion
Day of the week Module
CPTR-215
Prof. Ordonez
2017-08-31 - Thursday
Uses Zeller's Congruence (https://en.wikipedia.org/wiki/Zeller's_congruence)
'''

import math

#date = input('Enter date (yyyy-mm-dd): \n')
#date_list = date.split('-')


def nameForDayOfWeekNumber(code):
    '''
    Returns the name of the day provided
    :param code: INput of the day code
    :return: String containing day name
    >>> [nameForDayOfWeekNumber(5)]
    ['Thursday']
    '''

    day_dict = {

        2 : 'Monday',
        3 : 'Tuesday',
        4 : 'Wednesday',
        5 : 'Thursday',
        6 : 'Friday',
        7 : 'Sabbath',
        1 : 'Sunday',
    }
    return day_dict[int(code)]

def dayOfWeekForDate(year, month, day):
    '''
    Returns the number code for the day of the week on a given day
    :param year: Input for given year
    :param month: Input for given month
    :param day:  Input for given day
    :return:
    >>> [dayOfWeekForDate(2017, 9, 7)]
    [5]
    '''
    Y = int(year)
    #J = int(year) / 100
    #K = int(year) % 100
    q = int(day)
    m = int(month)
    if (month == 1) or (month == 2):
        Y -= 1
        m += 12
    h = (q + 13 * (m + 1) / 5 + Y + Y // 4 - Y // 100 + Y // 400) % 7
    #h = (q + 13 * (m + 1) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
    if h == 0:
        h = 7
    return int(h)


if __name__ == "__main__":
    import doctest
    doctest.testmod()