from sys import argv
from collections import Counter

if (len(argv) != 2):
    print "Usage: %s <inputstring>" % argv[0]
else:
    inputstring = argv[1]
    print "Input string:", inputstring
    inputcharlist = list(inputstring)
    print "Input char list:", inputcharlist

    c = Counter(inputcharlist)
    print list(c.elements())

    myfile = open( "data.in", "r" )
    for line in myfile:
        inputCnt = c
        word = line.strip()
        wordCnt = Counter(list(word))
    
        print word
        print list(inputCnt.elements())
        print list(wordCnt.elements())

        remainingCnt = wordCnt - inputCnt
        print list(remainingCnt.elements())
        if remainingCnt.values() == []:
            print "Word matches: %s" % word
        print

    myfile.close()
  
