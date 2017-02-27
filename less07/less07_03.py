try:
    file1 = open("file1.txt")
    for line in file1:
        int(line)
except ValueError as e:
    print(e)
else:
    print("I did it!")
finally:
    file1.close()
    print("Closing file...")
