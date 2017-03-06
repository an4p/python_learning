#newFile = open("newFile.txt", 'a')
file = open("fileForReading.txt", 'r+')

for line in file:
    #line = file.readline().strip() #it does not correct
    print(line.rstrip() + "!")
#print(type (file))


#type (file)

print("ddfasdffasf", "dfasfd", 5, file = file, sep='*')
print("ddfasdffasf", "dfasfd", 5, file = file, sep='\n')
file.close()