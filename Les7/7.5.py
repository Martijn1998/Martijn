def namen():
    dictionary = {}
    naam = None
    while True:
        naam = (input ('Volgende naam: '))
        if (naam is ''):
            break
        elif naam in dictionary.keys():
            aantal = dictionary[naam]
            dictionary[naam] = aantal + 1
        else:
            dictionary[naam] = 1
    for x in dictionary:
        if dictionary[x] == 1:
            print('Er is 1 student met de naam {}.'.format (x))
        else:
            print('Er zijn {} studenten met de naam {}.'.format(dictionary[x], x))

namen()