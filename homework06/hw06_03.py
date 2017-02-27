userFile = open("file_read.txt")
words = []
for line in userFile:
    tmp = line.split()
    for t in tmp:
        words.append(t.lower().strip(".").strip(",").strip("-").strip("*").strip("!"))
words = set(words)
words = list(words)
words.sort()
for word in words:
    print(word)