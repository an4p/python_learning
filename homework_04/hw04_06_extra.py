import sys
arg1 = sys.argv[1]
userFile = open(arg1)
lines = userFile.readlines()
counter = 0
for item in lines:
    counter += int(item.lower().count("we"))
print(counter)