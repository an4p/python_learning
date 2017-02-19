userString = input("Enter a number:\n")
# check for a letters only. It should be rewritten
#while userString.isalpha():
#     print("Please, enter a NUMBER \n")
#     userString = input()
userString = float(userString)
if userString > 0:
    print("+")
elif (userString < 0):
    print("-")
else:
    print("there is no sign in this number")
