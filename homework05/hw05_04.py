l = ["abc", 1, 2, 3, "ab", "bc", "abc", 12]
value = "abc"
countValue = l.count(value)
for i in range(countValue):
    l.remove(value)
print(l)
