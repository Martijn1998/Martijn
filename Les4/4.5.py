def kwadratenSom(grondgetallen):
    uitkomst = 0
    for getal in grondgetallen:
        if getal > 0:
            uitkomst += getal ** 2
    return uitkomst

grondgetallen = [4, 5, 3, -81]

print(kwadratenSom(grondgetallen))