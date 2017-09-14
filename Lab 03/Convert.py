'''
Julian Ancion
Prof. Ordonez
CPTE-215-A
9-13-17
Lab 03 - Convert!
'''

def wordsFromNumber(num):
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
    }
    sect_three = {
        3: 'hundred',
        4: 'thousand',
        7: 'million',
        10: 'billion',
        13: 'trillion',
        16: 'quadrillion',
        19: 'quintillion'
    }

    string = ''
    string_list = []
    num_str = str(num)

    for i in num_str:
        string_list.append(i)

    print(len(num_str))
    if len(num_str) <= 3:
        string = sect_one[sect_one[num]]
    if len(num_str) <= 4:
        pass
    if len(num_str) <= 7:
        pass
    if len(num_str) <= 10:
        pass
    if len(num_str) <= 13:
        pass
    if len(num_str) <= 16:
        pass
    if len(num_str) <= 19:
        pass

    print(string)






wordsFromNumber(10000000)