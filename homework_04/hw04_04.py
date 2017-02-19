userStr = input("Please, enter an integer positive number\n")
while not userStr.isdigit():
    print("This is not an integer positive number")
    userStr = input("Please, enter an integer NUMBER\n")
userStr = int(userStr)
factorial = 1
for item in range(1, userStr + 1):
    factorial *= item
print("The factorial of ", userStr, " is ", factorial)
userStr = input("Please, enter an integer number")
