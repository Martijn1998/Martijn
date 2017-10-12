import time
import csv

bestand = 'inloggers.csv'

def inloggen():
    with open(bestand, 'a') as f:
        while True:
            tijd = time.strftime('%a %d %b %y at %H %M', time.localtime())
            naam = input("Wat is je achternaam? ")
            if naam == 'einde' or naam == 'Einde':
                break
            voorl = input("Wat zijn je voorletters? ")
            gbdatum = input("Wat is je geboortedatum? ")
            email = input("Wat is je e-mail adres? ")

            gegevens = tijd + ';' + naam + ';' + voorl + ';' + gbdatum + ';' + email
            f.write(gegevens)
            f.write('\n')


inloggen()