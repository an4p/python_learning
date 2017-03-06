def is_date(day, month, year):
    import hw08_05
    month31 = [1, 3, 5, 8, 10, 12]
    month30 = [4, 6, 7, 9, 11]
    if day <= 0:
        return False
    if (month <=0) or (month > 12):
        return False
    if month in month31:
        if day > 31:
            return False
    if month in month30:
        if day > 30:
            return False
    if month == 2:
        if hw08_05.is_year_leap(year):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    return True

#print(is_date(29, 2, 2001))
