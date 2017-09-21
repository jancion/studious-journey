'''
Julian Ancion
CPTR-215
Prof. Ordonez
2017-08-31 - Thursday
Uses Zeller's Congruence (https://en.wikipedia.org/wiki/Zeller's_congruence)
'''

import math
date = input('Enter date (yyyy-mm-dd): \n')
date_list = date.split('-')


def weeker(code):

    day_dict = {

        2 : 'Monday',
        3 : 'Tuesday',
        4 : 'Wednesday',
        5 : 'Thursday',
        6 : 'Friday',
        0 : 'Sabbath',
        1 : 'Sunday',
    }
    return day_dict[int(code)]

def calculate(year, month, day):
    Y = int(year)
    #J = int(year) / 100
    #K = int(year) % 100
    q = int(day)
    m = int(month)
    if (month == '01') or (month == '02'):
        Y -= 1
        m += 12
    h = (q + 13 * (m + 1) / 5 + Y + Y // 4 - Y // 100 + Y // 400) % 7
    #h = (q + 13 * (m + 1) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
    print(weeker(h), end='')


calculate(date_list[0], date_list[1], date_list[2])