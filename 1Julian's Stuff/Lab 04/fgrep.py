#!/root/Downloads/Python-3.7.0a1/python
'''
Julian Ancion & Prof. Ordonez
CPTR-215-A
09/20/17
fgrep
'''
import sys


def fgrep():
    '''
    Usage: ./fgrep.py PATTERN [FILE] [FILE2]...
    Searches for string within file or string depending on number of inputs.
    :return: Returns nothing but prints string where pattern is found.

    '''
    if len(sys.argv) == 1:
        print('Usage: ./fgrep.py PATTERN [FILE]...')

    elif len(sys.argv) == 2:
        while True:
            try:
                string = input()
                if sys.argv[1] in string:
                    print(string)
            except EOFError:
                return '\n\n'

    elif len(sys.argv) == 3:
        string = sys.argv[1]
        for fileName in sys.argv[2:]:
            fileStream = open(fileName, "r")
            for line in fileStream:
                if string in line:
                    print(line, end='')

            fileStream.close()
    else:
        string = sys.argv[1]
        for fileName in sys.argv[2:]:
            fileStream = open(fileName, "r")
            for line in fileStream:
                if string in line:
                    print(fileName + ':', line, end='')

            fileStream.close()


if __name__ == '__main__':
    fgrep()

