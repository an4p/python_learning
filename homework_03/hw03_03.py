while (True):
    print("Type 'quit' to exit")
    phrase = input("Your message: ")
    if phrase == "quit":
         break
    elif phrase == "Hello" or phrase == "Hi":
        print("Hi! How's it going?")
    elif phrase == "What is your name?":
        print("I don't have a name :(")
    elif phrase == ("I am tired") or phrase == ("I'm tired"):
        print("Don't you want to speak with me any more?")
        phrase2 = input()
        if phrase2 == "No":
            print("Please, talk with me for a while")
        elif phrase2 == "Yes":
            print == "Nice"
    else:
        print("I don't understand you")