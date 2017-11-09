f = open('iplist.txt', 'r')

for line in f:
    sline = line.split('.')
    if len(sline) == 3:
        sline[2] = sline[2].strip()
        sline.insert(3, '0/24')
    print(sline[0] + '.' + sline[1] + '.' + sline[2] + '.' + sline[3])

f.close()