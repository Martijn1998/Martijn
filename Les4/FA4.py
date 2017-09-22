def standaardprijs(afstandKM):
    totaalPrijs = 0
    if afstandKM < 50:
        kmPrijs = 0.8
        totaalPrijs += kmPrijs * afstandKM
        return(totaalPrijs)
    if afstandKM > 50:
        totaalPrijs = totaalPrijs + 15
        kmPrijs = 0.6
        totaalPrijs += kmPrijs * afstandKM
    return totaalPrijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    totaalPrijs = standaardprijs(afstandKMInp)
    print(totaalPrijs)
    # Leeftijd
    if leeftijd >= 12 and leeftijd <= 65:

        if weekendRit == 'j':
            TP2 = totaalPrijs / 0.35
            return TP2

        else:
            TP2 = totaalPrijs / 0.3
            return TP2


    else:
        if weekendRit == 'j':
            TP2 = totaalPrijs / 0.4
            return TP2

        else:
            #geen korting
            TP2 = totaalPrijs
            return TP2

afstandKMInp = eval(input('Hoeveel KM gaat u reizen?'))
weekendRit = input('Weekendrit? j/n')
leeftijd = int(input('Leeftijd: '))
ritprijs2 = ritprijs(leeftijd, weekendRit, afstandKMInp)
print(ritprijs2)
