def power(a, n):
    """
    (float, int) -> float

     Returns a power n
    """
    if n == 1:
        return a
    else:
        return a * power(a, n-1)

print(power(2, 5))