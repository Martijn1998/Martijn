import xmltodict

with open('FA10.xml') as fd:
    doc = xmltodict.parse(fd.read())

    print('Dit zijn de codes en types van de {} stations: '.format(len(doc['Stations']['Station'])))
    for station in doc['Stations']['Station']:
        print('{:4} - {}'.format(station['Code'], station['Type']))
    print()

    print('Dit zijn alle stations met een of meer synoniemen: ')
    for station in doc['Stations']['Station']:
        if station['Synoniemen'] is not None:
            print('{:4} - '.format(station['Code']), end='')
            print(station['Synoniemen'])
            print()

    print('Dit is de lange naam van elk station: ')
    for station in doc['Stations']['Station']:
        print('{:4} - '.format(station['Code']), end='')
        print(station['Namen']['Lang'])