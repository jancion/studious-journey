import os, subprocess
os.system('ls /home >homeusers.out')
f = open('homeusers.out', 'r')
for line in f:
    x = line.strip()
    y = str(subprocess.check_output('groups ' + x, shell=True)).strip()
    z = (y.split(':'))
    z2=z[1].split(' ')
    if len(z2) > 2:
        print(y[2:-3])
f.close()