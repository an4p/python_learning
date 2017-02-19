userStr = input("Please, enter some text ")
print(userStr)
for i in range(len(userStr)):
    userStr = userStr[0: -1]
    print(userStr)
