knownWords = []
while True:
    userInput = input("Enter one word only: \n").split()
    userInput = [x.lower() for x in userInput]
    if len(userInput) != 1:
        continue
    else:
        if userInput[0] in knownWords:
            print("This word is known!")
            continue
        print("Thank you")
        knownWords.append(userInput[0])
 #   print(knownWords)

