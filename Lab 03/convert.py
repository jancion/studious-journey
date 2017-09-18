2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24


def groupedByThrees(number):
    """
    >>> groupedByThrees(123)
    ['123']
    >>> groupedByThrees(456)
    ['456']
    >>> groupedByThrees(78)
    ['078']
    >>> groupedByThrees(9)
    ['009']
    >>> groupedByThrees(1234)
    ['001', '234']
    >>> groupedByThrees(12345678901234567890)
    ['012', '345', '678', '901', '234', '567', '890']
    """
    numStr = str(number)
    while len(numStr) % 3 != 0:
        numStr = '0' + numStr
    return [numStr[index: index + 3] for index in range(0, len(numStr), 3)]


def wordsFromNumber(number):
    '''
    Takes a integer and converts it into words.
    :param number: the number to be converted
    :return: string containing words converted from integer
    >>> wordsFromNumber(1999999)
    'one million nine hundred ninety-nine thousand nine hundred ninety-nine'
    '''
    if number == 0:
        return 'zero'
    ones = {
        '0': '',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    oneties = {
        '0': 'ten',
        '1': 'eleven',
        '2': 'twelve',
        '3': 'thirteen',
        '4': 'fourteen',
        '5': 'fifteen',
        '6': 'sixteen',
        '7': 'seventeen',
        '8': 'eighteen',
        '9': 'nineteen'
    }
    tens = {
        '0': '',
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'
    }
    biggens = {
        '0': '',
        '1': 'hundred',
        '2': 'thousand',
        '3': 'million',
        '4': 'billion',
        '5': 'trillion',
        '6': 'quadrillion',
        '7': 'quintillion',
        '8': 'septillion'
    }
    numList = groupedByThrees(number)
    count = len(numList)
    string = ''





    for slice in numList:
        track = 0
        teen = False
        for digit in slice:
            if (digit == '0') and (track == 0):
               track += 1
            else:
                if track == 0:
                    if digit != '0':
                        string += ones[digit] + ' ' + biggens['1'] + ' '
                    track += 1
                elif track == 1:
                    if digit == '1':
                        teen = True
                        track += 1
                    else:
                        num = digit
                        track += 1
                elif track == 2:
                    if teen == True:
                        string += oneties[digit] + ' '
                    elif digit != '0':
                        if num != '0':

                             string += tens[num] + '-' + ones[digit] + ' '

                        else:
                            if digit != '0':
                                string += ones[digit] + ' '


                    else:
                        if num != '0':
                            string += tens[num] + ' '






        if (count > 1) and (slice != '000'):
            string += biggens[str(count)] + ' '
        count -= 1
    string = string[:-1]
    return string

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #print(wordsFromNumber(0))

