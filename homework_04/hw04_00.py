l = [1, "a", "Hello", 2.2]
for i in range(len(l)):
    print(type(l[i]), end=" ")
    if type(l[i]) != str:
        l[i] = str(l[i])
        print("cast to ", type(l[i]), end=" ")
    else:
        print("nothing to do...", end=" ")
    print()

