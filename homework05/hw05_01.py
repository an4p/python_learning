#1st way
varFileRead = open("file_read.txt", 'r')
varFileWrite = open("file_write.txt", 'w')
counter = 1
for line in varFileRead:
    print(str(counter) + " " + line.rstrip(), file=varFileWrite)
    counter +=1
varFileRead.close()
varFileWrite.close()

#2nd way
varFileRead = open("file_read.txt", 'r')
varFileWrite2 = open("file_write2.txt", 'w')
phrases = varFileRead.readlines()
phrases2 = [str(phrases.index(phrase) + 1) + "  " + phrase for phrase in phrases]
varFileWrite2.writelines(phrases2)
varFileRead.close()
varFileWrite2.close()

