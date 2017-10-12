
def seizoen(maand):
    if maand ==1 or maand ==2 or maand ==12:
        return 'winter'
    if maand ==3 or maand==4 or maand==5:
        return 'lente'
    if maand ==6 or maand==7 or maand==8:
        return 'zomer'
    if maand ==9 or maand==10 or maand==11:
        return 'herfst'


maand = int(input('welk nummer van de maand is het?'))
antwoord = seizoen(maand)
print(antwoord)

