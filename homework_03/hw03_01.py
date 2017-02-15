import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]

if arg1 > arg2:
    result = float(arg1) - float(arg2)
elif arg1 < arg2:
    result = float(arg1) + float(arg2)
else:
    result = arg1
print(result)

