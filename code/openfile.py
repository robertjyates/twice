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
        word = line.strip()
        print word
    myfile.close()
  
