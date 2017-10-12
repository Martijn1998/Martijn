import csv

with open('artikelen.csv', 'w', newline='') as csvfile:
    fieldnames = ['Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    lijst = [[121,  'ABC123', 'Highlight pen', 231, 0.56], [123, 'PQR678', 'Nietmachine', 587, 9.99], [128,  'ZYX163', 'Bureaulamp', 34, 19.95], [137, 'MLK709', 'Monitorstandaard', 66, 32.50], [271, 'TRS665', 'Ipad hoes', 155, 19.01]]
    writer.writeheader()
    for list in lijst:
        writer.writerow({'Artikelnummer' : list[0], 'Artikelcode' : list[1], 'Naam' : list[2], 'Voorraad' : list[3], 'Prijs' : list[4] })