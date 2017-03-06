def is_year_leap(year):

    if (year % 4 != 0):
        return False
    elif (year % 400 == 0):
        return True
    elif (year % 4 == 0) & (year % 100 == 0):
        return False
    else:
        return True

#print(is_year_leap(2100))