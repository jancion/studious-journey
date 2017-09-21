# !/usr/local/bin/python3

# 4b-wc.py
# Robert Ordonez & CPTR-215
# 2017-09-18 first draft - single file, command-line argument
# 2017-09-20 multiple files from command-line arguments plus totals
import sys


def countFile(file):
    numLines = numWords = numChars = 0
    for line in file:
        numLines += 1
        numWords += len(line.split())
        numChars += len(line)
    return (numLines, numWords, numChars)


if len(sys.argv) == 1:
    numLines, numWord, numChars = countFile(sys.stdin)
    print("%8d%8d%8d" % (numLines, numWords, numChars))
else:
    totalLines = totalWords = totalChars = 0
    for fileName in sys.argv[1:]:
        fileStream = open(fileName, "r")
        numLines, numWord, numChars = countFile(fileStream)
        print("%8d%8d%8d %s" % (numLines, numWords, numChars, fileName))
        fileStream.close()
        totalLines += numLines
        totalWords += numWords
        totalChars += numChars
    if len(sys.argv) > 2:
        print("%8d%8d%8d total" % (totalLines, totalWords, totalChars))
