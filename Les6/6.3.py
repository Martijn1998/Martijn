invoer = '5-9-7-1-7-8-3-2-4-8-7-9'
list = invoer.rsplit('-')
intlijst = []

for getal in list:
    intlijst.append(int(getal))

intlijst.sort()
print('Gesorteerde list van ints:', intlijst)
print('Grootste getal:',max(intlijst), 'en Kleinste getal: ',min(intlijst))
print('Aantal getallen:',len(intlijst), 'en Som van de getallen:',sum(intlijst))
avg = sum(intlijst) / len(intlijst)
print('gemiddelde', avg)