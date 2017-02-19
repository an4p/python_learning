#some amazing thing from stepic.org
A, B = (int(ab) for ab in input("Enter two numbers with a space: \n").split())

if A > B:
    rangeAB = list(range(A, (B-1), -1))
    #print(rangeAB)
else:
    rangeAB = list(range(A, B + 1))
    #print(rangeAB)
for num in rangeAB:
    print(num, end=" ")