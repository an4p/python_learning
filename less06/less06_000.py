l = [x for x in input().split()]
listNew = []
counter = 0
for item in l:
    if len(item) >= 2 and item[0] == item[-1]:
        listNew.append(item)
        counter +=1
print(str(counter) + " words: ")
print(listNew)
