words = [x for x in input("Enter a phrase: \n").split()]

filteredList = [fl for fl in words if fl[0].lower() in ("a", "b", "c")]
print(filteredList)
print(filteredList, file=open("file05_02.txt", "w"))

for word in words:
    if word[0].lower() not in ("a", "b", "c"):
        continue
    else:
        print(word)
        print(word, file = open("file05_02a.txt", "a"))