#file from task 03
#varFileRead = open("file_read.txt", 'r')
#phrases = varFileRead.readlines()
phrases = ["abc", 1, 2, 3, "ab", "bc", "abc", 12]
phrasesLengh = [len(phrase) for phrase in phrases if type(phrase) == str]
print(phrasesLengh)
#varFileRead.close()