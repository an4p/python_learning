l = [1, 2, 2, 6, 5, 7, 8, 1, 2, 4, 3, 3, 5, 5]
list_new = []
#for item in l:
for i in range(len(l)):
    if (len(l) - i < 2):
        break
    if l[i] == l[i+1]:
        continue
    list_new.append(l[i])
print(list_new)