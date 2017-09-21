'''
Julian Ancion & Prof. Ordonez
CPTR-215-A
09/20/17
fgrep
'''

filename = ['test', 'testies']

import sys

def fgrep():
    for filename in sys.argv[1:]:
        print(filename)
