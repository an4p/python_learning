userList = ['a', '1', '-2', 'b', 'c', 'd', 3, 4, -5, 6, 7, 'e', 'ef', 'fdafs']
alfaList = []
numList = []

for item in userList:
    if (type(item) == int) or (type(item) == float):
        numList.append(item)
    elif type(item) == str:
        if str(item).isnumeric():
            #but what to do with negative integers?
            numList.append(int(item))
        else:
            alfaList.append(item)
    else:
        print("This element of the list neither number nor string")
print(alfaList)
print(numList)