file = open("fileForReading.txt", 'r+')
# line = file.readline()
# while line:
#     print(line, end="")
#     #it is impossible to print line+"!" because of new line
#     line = file.readline()


for line in file:
    #line = file.readline().strip() #it does not correct
    print(line.rstrip() + "!")
#print(type (file))


#type (file)

print("ddfasdffasf", "dfasfd", 5, file = file, sep='*')
print("ddfasdffasf", "dfasfd", 5, file = file, sep='\n')
file.close()