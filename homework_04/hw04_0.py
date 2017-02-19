file = open("fileForReading.txt")
line = file.readline()
while line:
    print(line, end="")
    #it is impossible to print line+"!" because of new line
    line = file.readline()
file.close()


