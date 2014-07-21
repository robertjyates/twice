from sys import argv
from collections import Counter

if (len(argv) != 2):
    print "Usage: %s <inputStr>" % argv[0]
else:
    inputStr = argv[1]
    inputCnt = Counter(inputStr)
    print "Input string:", inputStr
    #dictionaryFilenames = ["data.in"]
    dictionaryFilenames = ["../scowl-7.1/final/english-words.10",
                      "../scowl-7.1/final/english-words.20"]
    for filename in dictionaryFilenames:
        with open(filename, 'r') as f:
            for line in f:
                word = line.strip()
                wordCnt = Counter(word)
                remainingCnt = wordCnt - inputCnt
                if remainingCnt.values() == []:
                    print "Word matches: %s" % word

