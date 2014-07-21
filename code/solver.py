from sys import argv
from collections import Counter

if len(argv) != 2:
    print "Usage: %s <jumbled_word>" % argv[0]
else:
    inputStr = argv[1]
    inputCnt = Counter(inputStr)
    #dictionaryDirectory = "./"
    #dictionaryFilenames = ["data.in"]
    dictionaryDirectory = "../scowl-7.1/final/"
    dictionaryFilenames = ["english-words.10", "english-words.20"]
    for filename in dictionaryFilenames:
        with open(dictionaryDirectory + filename, 'r') as f:
            for line in f:
                word = line.strip()
                if word != inputStr:
                    wordCnt = Counter(word)
                    remainingCnt = wordCnt - inputCnt
                    if remainingCnt.values() == []:
                        print word

