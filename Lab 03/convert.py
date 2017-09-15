def groupedByThrees(number):
    '''
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
    '''
    #for i in map(int, [number]):
    #     += format(i, ',').split(',')

    numStr = str(number)
    while len(numStr) % 3 != 0:
        numStr = '0' + numStr

    numberStr = ['%03d' % number]
    return [numStr]




if __name__ == '__main__':
    import doctest
    doctest.testmod()