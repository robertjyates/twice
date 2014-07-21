import sys

if (len(sys.argv) != 2):
    print "Usage: %s <inputstring>" % sys.argv[0]
else:
    inputstring = sys.argv[1]
    print "Input string:", inputstring
    inputcharlist = list(inputstring)
    print "Input char list:", inputcharlist

    myfile = open( "data.in", "r" )
    mylist = []
    for line in myfile:
        mylist.append( line.strip() )
    myfile.close()
  
    for line in mylist:
        print line
