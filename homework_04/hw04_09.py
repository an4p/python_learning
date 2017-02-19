import random
#samples
#random.randrange(1000)
#round(random.random()*1000)
#random.randint(1,1000)

a, b = (int(x) for x in input("Enter 2 integer numbers with a space: \n").split())
if (a % b == 0) or (b % a == 0):
    print(1)
else:
    randomNum = random.randint(1, 1000)
    print(randomNum)


