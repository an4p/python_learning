 #playing around the list
l = [1,2,3,4,5]
l[2] = [1,4,6]
l2 = [100,100,100]
l[index] = l2[1]
index = round(len(l2))
l[index] = l2[1]
l[index:index] = 'a'
print(l*4)
l = l+l2
#l.append(l2)

print('spam' in l)
print('egg' not in l)

#with methods
l2 = l2.append([1,2,3])