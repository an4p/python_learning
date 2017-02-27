fd = open("fakeData.txt",  'r')
line1 = fd.readline()
data = []
for line in fd:
    #how to handle with empty line?
    if line:
        data.append(line.rstrip())
    print(line)
fd.close()
#for l in line1.split():

departments = set()
for d in data:
    if d:
        temp = d.split()
        #print(temp)
    else:
        continue
    departments.add(temp[2])
#print(departments)