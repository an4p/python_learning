UserString = str(input("Please, print a word or a phrase: "))

print(UserString[2], UserString[-2], UserString[0:6], UserString[0:(len(UserString)-2)],
      UserString[0::2], UserString[1::2], UserString[::-1], UserString[::-2], len(UserString), sep="\n")
