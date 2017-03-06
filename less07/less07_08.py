def abc(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a, b, c = 2, 3, 5
print(abc(a, b, c))
