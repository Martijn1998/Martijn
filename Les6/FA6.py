
def toon_aantal_kluizen_vrij():
     file = open('kluizen.txt')
     numLines = file.readlines()
     vrijeKluizen = 12 - len(numLines)
     if vrijeKluizen == 1:
         print('Er is 1 kluis beschikbaar.')
     else:
         print('Er zijn', vrijeKluizen, 'kluizen beschikbaar.')
     file.close()
     menu()


def nieuwe_kluis():
     listKluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
     file = open('kluizen.txt', 'r')
     for line in file:
         for Kluisnummer in listKluizen:
                if str(Kluisnummer) in line:
                    listKluizen.remove(Kluisnummer)
     if listKluizen == []:
         print('Er zijn geen lege kluizen beschikbaar.')
     else:
            wachtwoord = input('U krijgt kluis nr. {}. Voer nu een code in: '.format(listKluizen[0]))
            wachtwoord2 = input('Voer nogmaals uw code in ter controle: ')
            if wachtwoord != wachtwoord2:
                print('Het wachtwoord klopt niet. U krijgt geen kluis.')
            else:
                file = open('kluizen.txt', 'a')
                file.write("{0};{1}\n".format(listKluizen[0], wachtwoord))
                # file.write(str(listKluizen[0])+';'+wachtwoord)
                file.close()
                print('Klaar! Code {0} is toegwezen tot kluis nr. {1}'.format(wachtwoord, str(listKluizen[0])))
     menu()


def kluis_openen():
        file = open('kluizen.txt', 'r')
        Kluisnummer = input('Geef uw kluisnummer: ')
        wachtwoord = input('Geef de bijbehorende code voor de kluis: ')

        for line in file:
            if Kluisnummer + ';' + wachtwoord in line:
                print('U kunt nu uw kluis openen!')
            else:
                print('De ingevoerde gegevens kloppen niet.')

        file.close()
        menu()


def kluis_teruggeven():
     print('Functie niet mogelijk ;)')
     menu()


def menu():
     print('''\n\"Bagagekluis\". \nMaak een keuze:
     [1.]    Ik wil weten hoeveel kluizen nog vrij zijn.
     [2.]    Ik wil een nieuwe kluis.
     [3.]    Ik wil even iets uit mijn kluis halen.
     [4.]    Ik geef mijn kluis terug. (optioneel)
     [5.]    Log uit.''')

     optie = 0
     optie_lijst = [1, 2, 3, 4, 5]
     while optie not in optie_lijst:
         try:
             optie = int(input('>>> '))
             if optie not in optie_lijst:
                 print('Voer een waarde tussen 1 en 4 in!')
         except:
             print('Ongeldige input.')

     if optie == 1:
         print('optie 1.')
         toon_aantal_kluizen_vrij()
     elif optie == 2:
         print('optie 2.')
         nieuwe_kluis()

     elif optie == 3:
         print('optie 3.')
         kluis_openen()

     elif optie == 4:
         print('optie 4.')
         kluis_teruggeven()

     elif optie == 5:
         print('Tot ziens!')
         exit()

     else:
         print('Foutmelding!, \n Voer een getal tussen 1 en 4 in!')


menu()
