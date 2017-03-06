def min2(*args):
#    l = sorted(args)
    l = list(args)
    l.sort()
    return(l[1])
m = min2(1,2,3,0,9,2,-3,-5)
print(m)