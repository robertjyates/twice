myfile = open( "data.in", "r" )
mylist = []
for line in myfile:
    mylist.append( line.strip() )
myfile.close()

for line in mylist:
    print line
