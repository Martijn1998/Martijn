def string(list):
    list2 = []
    list3 = []
    for item in list:
        if len(item) == 4:
            list2.append(item)
    return list2

list = input('Geef lijst met minimaal 10 strings:').split()
print('De nieuw-gemaakte lijst met alle vier-letter strings is: ', string(list))