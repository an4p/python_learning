#file from task 03
varFileRead = open("file_read.txt", 'r')
phrases = varFileRead.readlines()
phrasesLengh = [len(phrase) for phrase in phrases if type(phrase) == str]
print(phrasesLengh)
varFileRead.close()