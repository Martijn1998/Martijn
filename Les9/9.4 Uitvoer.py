import csv
with open('artikelen.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    column = {}
    for h in headers:
       column[h] = []

    for row in reader:
        for h, v in zip(headers, row):
            if h == 'Artikelcode' or h == 'Naam':
                column[h].append(v)
            else:
                column[h].append(eval(v))
    duurste = column['Prijs'].index(max(column['Prijs']))
    print('Het duurste artikel is {} en die kost {:.2f} Euro.'.format(column['Naam'][duurste],column['Prijs'][duurste]))

    kleinste = column['Voorraad'].index(min(column['Voorraad']))
    print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(column['Voorraad'][kleinste], column['Artikelnummer'][kleinste]))

    print('In totaal hebben wij {} producten in ons magazijn liggen.'. format(sum(column['Voorraad'])))