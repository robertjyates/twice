from sys import argv
from collections import Counter

if (len(argv) != 2):
    print "Usage: %s <inputstring>" % argv[0]
else:
    inputstring = argv[1]
    print "Input string:", inputstring
    inputCnt = Counter(inputstring)
    print list(inputCnt.elements())
    print

    with open('data.in', 'r') as f:
        for line in f:
            word = line.strip()
            wordCnt = Counter(word)
            print word
            print list(wordCnt.elements())

            remainingCnt = wordCnt - inputCnt
            print list(remainingCnt.elements())
            if remainingCnt.values() == []:
                print "Word matches: %s" % word
            print

