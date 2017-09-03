'''
Julian Ancion
Prof. Ordonez
CPTR-215
2017-09-01
Calender Program
'''

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

def is_leap(year):

    '''
    A year will be a leap year if it is divisible by 4 but not by 100. If a year is divisible by 4 and by 100, it is not a leap year unless it is also divisible by 400.
    '''
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        return True
    else:
        return False

def build_caldener(year, month):
    date_input = input('Enter a date: ')
    date_input = date_input.split(' ')

    month_list = {
        '01' : 'January'
    }
print(date_input)
calculate(date_input[1], date_input[0], 1)
print(is_leap(int(date_input[1])))
