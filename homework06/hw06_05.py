userFile = open("file_read.txt")
words = []
for line in userFile:
    temp = line.lower().split()
    for t in temp:
        t = t.strip(".").strip(",").strip("!").strip("-").strip("*")
        if t.isalpha():
            words.append(t)
wordDict = {}
for word in words:
    if word in wordDict:
        wordDict[word] += 1
    else:
        wordDict.setdefault(word, 1)
for word, value in wordDict.items():
    print(word, ": ", value, " time(s)")