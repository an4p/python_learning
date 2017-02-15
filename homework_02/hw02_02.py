userInput = str(input("Please input something: "))
userInput1 = userInput[0:(len(userInput)+1)//2]
userInput2 = userInput[(len(userInput)+1)//2:]
userInputNew = userInput2+userInput1
print(userInputNew)