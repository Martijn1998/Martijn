getal = []
invoer = 1

while invoer != 0:
    getal.append(invoer)
    invoer = int(input('Voer een getal in: '))
    print('Er zijn {0} getallen ingevoerd. De som van de getallen is {1}'.format(len(getal)-1, sum(getal)))