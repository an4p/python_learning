import sys

#a = float(sys.argv[1])
#b = float(sys.argv[2])
#c = a * b
#print(c)
#tt
# word = sys.argv[1]
# num = int(sys.argv[2])
#
# print(word * num)

# import math
#
# sq = float(sys.argv[1])
# result = math.sqrt(sq)
# print(result)

from math import sin, cos, pi
#import math  # it doesn't work with sin and cos without math.sin, math.cos
x = float(sys.argv[1])
one = sin(x)**2 + cos(x)**2
print(one)

