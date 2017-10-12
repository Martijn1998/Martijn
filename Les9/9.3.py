import csv

with open('scores.csv', 'r') as csvfile:
    x = csv.reader(csvfile, delimiter=';')
    hoogste = ['', '', 0]
    for y in x:
        if int(y[2])> int(hoogste[2]):
            hoogste = y
    print('De hoogste score is:{} op {} behaald door {}'.format(hoogste[2],hoogste[1],hoogste[0]))
