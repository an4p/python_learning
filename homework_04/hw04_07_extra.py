import sys

arg1 = sys.argv[1]

userFile = open(arg1)
lines = userFile.readlines()
userFile.close()

numList = []
for line in lines:
    words = line.split()
    for word in words:
        word = word.strip(",")
        word = word.strip(".")
        if word.isnumeric():
            numList.append(word)
print(numList)