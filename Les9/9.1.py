while True:
    try:
        bedrag = 4356
        groep = int(input('geeft aantal personen aan: '))
        kosten = bedrag / groep

        if groep < 0:
            raise TypeError
        print(kosten)
        break

    except ValueError:
        print ('Gebruik cijfers voor het invoeren van het aantal!')
    except ZeroDivisionError:
        print ('Delen door nul kan niet!')
    except TypeError:
        print ('Negatieve getallen zijn niet toegestaan!')
    except:
        print('Onjuiste invoer!')