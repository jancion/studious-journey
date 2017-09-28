'''
Julian Ancion
Prof. Ordonez
CPTE-215-A
9-13-17
Lab 03 - Convert!
'''

def wordsFromNumber(num):
    string_return = ''
    sect_one = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        0: 'zero'
    }
    sect_one_two = {
        1 : 'eleven',
        2 : 'twelve',
        3 : 'thirteen',
        4 : 'fourteen',
        5 : 'fifteen',
        6 : 'sixteen',
        7 : 'seventeen',
        8 : 'eighteen',
        9 : 'nineteen'
    }
    sect_two = {
        10: 'ten',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',

    }
    sect_three = {
        1: 'hundred',
        2: 'thousand',
        3: 'million',
        4: 'billion',
        5: 'trillion',
        6: 'quadrillion',
        7: 'quintillion'
    }

    num_list = []
    print(num_list)
    for i in map(int, [num]):
        num_list += format(i, ',').split(',')

    print(num_list)

    for i in num_list:
        print(num_list.index(i))




wordsFromNumber(1111111)