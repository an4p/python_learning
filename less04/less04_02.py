l = ["a","b","c",1,2,3,4]

for item in l:
    print(item, end=" ")

for s in "one", "two", "tree":
    print(s)

range(5)

w = "Hello"


result = 0
for i in range(1,100,2):
    result += i**2
print(result)


l2 = ['ds','a',2,3,4,5]

for item in l2[0:5]:
    print(item)
    #print item

list3 = [1, 2, 3, [1, 2, 3], 'a']
#home
for item in list3:
    if type(list3[item]) != str:
        list3[item] = str(item)
print(list3)