import xmltodict

with open('producten.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for x in doc['artikelen']['artikel']:
        print(x['naam'])