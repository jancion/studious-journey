'''
Julian Ancion
Prof. Ordonez
CPTR-215
2017-09-01
Calender Program
'''


def startingDayOfWeek(month, year):
    '''
    Used to determine what day of the week the first day of the month is.
    outputs the number code for the day.
    :param year: The year which is set to Y
    :param month: The month which is set to m
    :param day: The day which is set to q
    :return: h the number code for the day of the week

    >>> startingDayOfWeek(2, 2000)
    3
    >>> startingDayOfWeek(7, 1991)
    2
    '''

    Y = int(year)
    q = 1
    m = int(month)
    if (month == 1) or (month == 2):
        Y -= 1
        m += 12
    h = (q + 13 * (m + 1) // 5 + Y + Y // 4 - Y // 100 + Y // 400) % 7

    if int(h) == 0:
        return 7

    return int(h)


def daysInMonth(month, year):
    '''
    Returns the month and declares the month_list to be global and checks leap year for February.
    :param month: number index for month
    :param year: year number for checking leap year
    :return: returns month.

    >>> daysInMonth(1, 1991)
    31
    >>> daysInMonth(2, 2000)
    29
    '''
    global month_list
    month = str(month)
    month_list = {
        '1': ['January', 31],
        '2': ['February', 28],
        '3': ['March', 31],
        '4': ['April', 30],
        '5': ['May', 31],
        '6': ['June', 30],
        '7': ['July', 31],
        '8': ['August', 31],
        '9': ['September', 30],
        '10': ['October', 31],
        '11': ['November', 30],
        '12': ['December', 31]
    }
    if (year % 4 == 0) and (year % 100 != 0):
        month_list['2'] = ['February', 29]
        output = month_list[month][1]
    elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        month_list['2'] = ['February', 29]
        output = month_list[month][1]
    else:
        output = month_list[month][1]

    return output


def monthCalendarFor(month, year):
    '''
    Builds and returns a calender for the given month and year
    :param year: Year to be printed
    :param month: Month to be printed
    :return: a formatted calender with 0 extra whitespace

    >>> monthCalendarFor(7, 1991)
    '     July 1991\\nSu Mo Tu We Th Fr Sa\\n    1  2  3  4  5  6\\n 7  8  9 10 11 12 13\\n14 15 16 17 18 19 20\\n21 22 23 24 25 26 27\\n28 29 30 31\\n\\n'
    >>> monthCalendarFor(2, 1981)
    '   February 1981\\nSu Mo Tu We Th Fr Sa\\n 1  2  3  4  5  6  7\\n 8  9 10 11 12 13 14\\n15 16 17 18 19 20 21\\n22 23 24 25 26 27 28\\n\\n\\n'
    '''


    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'}

    row1 = months[month]
    row1 = str(row1) + ' ' + str(year)
    row1 = row1.center(20, ' ')
    row1 = row1.rstrip() + '\n'

    row2 = 'Su Mo Tu We Th Fr Sa\n'
    row_days = ''
    rowstart = (startingDayOfWeek(month, year))

    count = 0

    for i in range(1, daysInMonth(month, year) + 1):
        if len(str(i)) == 1:
            i = str(i) + ' '
        row_days += str(i) + ' '
        if (len(row_days) == 27) and (count == 0):
            row_days = row_days[:-1]

    if rowstart == 7:
        row3_5 = '                   '
    elif rowstart == 1:
        row3_5 = ' '
    elif rowstart == 2:
        row3_5 = '    '
    elif rowstart == 3:
        row3_5 = '       '
    elif rowstart == 4:
        row3_5 = '          '
    elif rowstart == 5:
        row3_5 = '             '
    elif rowstart == 6:
        row3_5 = '                '

    for i in row_days:
        row3_5 += i

        if (len(row3_5) == 21) or (len(row3_5) == 42 or len(row3_5) == 63) or (len(row3_5) == 84) or (len(row3_5) == 105):
            row3_5 = row3_5[:-1]
            row3_5 += '\n'

    if rowstart == 7:
        row3_5 = row3_5[:-1] + '\n'
    elif (month == 2) and ('29' not in row_days):
        row3_5 = row3_5[:-1] + '\n\n\n'
    else:
        row3_5 = row3_5[:-1] + '\n\n'
    output = row1 + row2 + row3_5
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod()

