
def changer(c_list):
    c_list[0],c_list[-1] = c_list[-1], c_list[0]
    print(c_list)


l = [1,2,3,4,5,6,7]
changer(l)

