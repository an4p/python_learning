varFileRead = open("file_read.txt", 'r')
wordList = []

for line in varFileRead:
    tempList = []
    tempList.extend(line.lower().split())
    for l in tempList:
        if l.isalpha():
            # wordList.extend(l) doesn't work correctly for this case
            wordList.append(l)
print(wordList, end="\n")





#phrases = varFileRead.readlines()
#words = [phrase.lower().split() for phrase in phrases if phrase.isalpha()]
#print(words)
varFileRead.close()