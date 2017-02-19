userNumList = [0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7]
counterPos = 0
counterNeg = 0
counterZero = 0
for item in userNumList:
    if item == 0:
        counterZero += 1
    elif item > 0:
        counterPos += 1
    else:
        counterNeg += 1
print("Positive numbers in list: ", counterPos)
print("Negative numbers in list: ", counterNeg)
print("Zeros in list:", counterZero)


