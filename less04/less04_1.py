i = 1
while i <= 10:
    # print(i, "fish in the aquarium")
    i += 1
k = 0
mylist = ['a', 'b', 'c', 'd']
while k < len(mylist):
   # print(mylist[k] + '!')
    k += 1

#not finished task
mystr = "alkdjfajfda"
mystr = list(mystr)
while mystr:
    del mystr[-1]
    #print(mystr)

#easier way
l = [1,2,3,4,5,6,7,8]
while l:
    l.remove(l[-1])
    #print(l)

l2 = [1,2,3,4,5,6,7,8,9]
while l2:
    #l2.pop() #delete last item of the list
    l2.pop(0) #delete first item of the list
    #print(l2)

str2 = "abcdefghij"
while str2:
    print(str2[-1])
    str2 = str2[0:-1]
    