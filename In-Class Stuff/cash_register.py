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
    if (month == '01') or (month == '02') or (month == '1') or (month == '2'):
        Y -= 1
        m += 12
    h = (q + 13 * (m + 1) / 5 + Y + Y // 4 - Y // 100 + Y // 400) % 7
    #h = (q + 13 * (m + 1) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
    return h

def is_leap(year):
    year = int(year)
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

    month_list = {
        '1' : ['January', 32],
        '2' : ['February', 29],
        '3' : ['March', 32],
        '4' : ['April', 31],
        '5' : ['May', 32],
        '6' : ['June', 31],
        '7' : ['July', 32],
        '8' : ['August', 32],
        '9' : ['September', 31],
        '10' : ['October', 32],
        '11' : ['November', 31],
        '12' : ['December', 32]
    }

    if is_leap(year) == True:
        month_list['2'] = ['February', 30]

    row1 = (month_list[month][0] + ' ' + str(year))
    row1 = row1.center(20, ' ')
    row1 = row1.rstrip()

    row2 = 'Su Mo Tu We Th Fr Sa'
    row_days = ''
    rowstart = (calculate(year, month, 1))

    rowstart = int(rowstart)

    count = 0
    for i in range(1, month_list[month][1]):
        if len(str(i)) == 1:
            i = str(i) + ' '
        row_days += str(i) + ' '
        if (len(row_days) == 27) and (count == 0):
            row_days = row_days[:-1]



    if rowstart == 0:
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

        if (len(row3_5)== 21) or (len(row3_5)== 42 or len(row3_5)== 63) or (len(row3_5)== 84) or (len(row3_5)== 105):
            #if row3_5[:-1] == ' ':
            row3_5 = row3_5[:-1]
            row3_5 += '\n'
    if rowstart == 0:
        row3_5 = row3_5[:-1] + '\n'
    else:
        row3_5 = row3_5[:-1] + '\n\n'




    print(row1)
    print(row2)
    print(row3_5, end="")

date_input = input()
date_input = date_input.split(' ')

build_caldener(date_input[1], date_input[0])