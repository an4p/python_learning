userWords = str(input("Please, enter 2 words: "))
wordsList = userWords.split(sep=" ")
wordsListNew = wordsList[1]+wordsList[0]
print(wordsListNew)