#!/root/Downloads/Python-3.7.0a1/python
'''
julian ancion
Dr. Beckett
stuff
'''

import os, subprocess


os.system("ls /home > homeusers.out")
f = open("homeusers.out", "r")
for line in f:
    x = line.strip()
    y = str((subprocess.check_output('groups ' + x, shell=True)))
    print(y[2:-3])


f.close()
