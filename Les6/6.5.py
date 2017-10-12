def tafels():
    x = 1
    y = 1
    k = 1
    while x <= 10 and y <= 10:
        f = x * y
        print(f)
        y = y + 1
    x = x + 1


tafel = 1 * tafels()
print (tafel)