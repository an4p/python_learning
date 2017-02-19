userFile = open("we.txt")
lines = userFile.readlines()
counter = 0
for item in lines:
    counter += int(item.lower().count("we"))
print(counter)