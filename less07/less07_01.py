s, i = 's', 0
try:
    s = int(s) / i
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print('Zero Division Error')