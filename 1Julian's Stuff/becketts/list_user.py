#!/usr/bin/python
'''
Julian Ancion
Dr. Beckett
CPTE-440 Test
User List
'''

import subprocess

user_list = subprocess.getoutput('cat /etc/passwd')
user_list = user_list.split('\n')

shell_list = subprocess.getoutput('cat /etc/shells')
shell_list = shell_list.split('\n')

for i in user_list:
        i = i.split(':')
        if i[-1] in shell_list:
                output = i[0] + '     ' + i[-1]
        else:
                output = i[0] + '     No shell'
        print(output)
