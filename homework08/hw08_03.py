def distance(x1, y1, x2, y2):
    '''
    (float, float, float, float) -> float

    Calculates distance between point(x1, y1) and (x2, y2)
    '''
    import math
    d = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
    return d

while(True):
    d = input("Enter float coordinates of point A(x1, y1) and B(x2 y2)): \n").split()
    for el in range(len(d)):
        try:
            d[el] = float(d[el])
            print(d[el])
        except:
            print("An error occured.")
    break
ab = distance(*d)
print(ab)