month = 'July'
year = 2017
days = 'Su Mo Tu We Th Fr Sa'
string = '01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 28 29 30 31'
list = ''
for i in string:
    list += i
    if (len(list) == 20) or (len(list) == 39) or (len(list) == 59) or (len(list) == 79):
        list += '\n'

print(list)