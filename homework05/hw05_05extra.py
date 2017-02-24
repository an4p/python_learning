varFileRead = open("file_read.txt", 'r')
wordList = []

for line in varFileRead:
    tempList = line.lower().split()
    for l in tempList:
        l = l.strip(".").strip(",")
        if l.isalpha():
            wordList.append(l)
print(wordList, end="\n")





#phrases = varFileRead.readlines()
#words = [phrase.lower().split() for phrase in phrases if phrase.isalpha()]
#print(words)
varFileRead.close()