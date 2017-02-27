userFile = open("file_read.txt", 'r')
words = []
uniqueWords = {}

for line in userFile:
    tempList = line.lower().split()
    for l in tempList:
        l = l.strip(".").strip(",")
        if l.isalpha():
            words.append(l)
for word in words:
    if word in uniqueWords:
        uniqueWords[word] += 1
    else:
        uniqueWords.setdefault(word, 1)
print(uniqueWords)

counter = 0
for uWord in uniqueWords:
    counter += int(uniqueWords[uWord])
print(counter)

