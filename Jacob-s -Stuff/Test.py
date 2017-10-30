#!/usr/bin/python3
file = open('/etc/passwd', 'r')
for line in file:
    sline = line.split(':')
    printvar = sline[0] + '     '
    if str(sline[-1]) == '/bin/bash\n':
        printvar += sline[-1]
    else:
        printvar += "No Shell"
    print(printvar)