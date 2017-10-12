def inlezen_beginstation(stations):
    while True:
        start = input('Vul hier een beginstation in: ')
        if start in stations:
            print('Uw beginstation is', start)
            return start
        else:
            print('Vul een ander station in.')


def inlezen_eindstation(stations, beginstation):
    while True:
        eind = input('Vul hier uw eindstation in: ')
        if eind in stations:
            if stations.index(beginstation) < stations.index(eind):
                print('Uw eindstation is', eind)
                return eind
        else:
            print('Dit kan niet, vul een ander station in.')


def omroepen_reis(stations, beginstation, eindstation):
    afstand = stations.index(eindstation) - stations.index(beginstation)
    prijs = afstand * 5
    print(
        'Het beginstation {} is het {}e station op het traject.'.format(beginstation, stations.index(beginstation) + 1))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindstation, stations.index(eindstation) + 1))
    print('De afstand bedraagt {} station(s).'.format(afstand))

    print('De prijs van het kaartje is {} euro.'.format(prijs))
    print('jij stapt in de trein in: {}'.format(beginstation))
    print('Met tussenstations:')
    for y in stations[stations.index(beginstation) + 1: stations.index(eindstation)]:
        print(y)
    print('Jij stapt uit in: {}'.format(eindstation))


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard',
            'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)