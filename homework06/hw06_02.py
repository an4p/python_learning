file1 = open("file_read.txt", "r")
file2 = open("read_file2.txt", 'r')

list1 = []
list2 = []
lists = [list1, list2]
files = [file1, file2]

counter = 0

for f in files:
    for line in f:
        tempList = line.lower().split()
        for l in tempList:
            l = l.strip(".").strip(",")
            if l.isalpha():
                lists[counter].append(l)
    counter +=1
list1 = set(list1)
list2 = set(list2)

print("The same words:")
print(list1.intersection(list2))
print("The unique words from 1st file:")
print(list1.difference(list2))