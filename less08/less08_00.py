from triangle import hypotenuse

c = [(3,4), (4,4), (1,2)]
for catet in c:
    result = hypotenuse(*catet)
    print("hypotenuse for ", str(catet), "is ", str(result))