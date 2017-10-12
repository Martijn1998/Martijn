
f = open('kaartnummers.txt','r')
content = []

for line in f:
    data = line.strip().split(',')
    print('\n {1} heeft kaartnummer: \n  {0}'.format(data[0], data[1],))


f.close()
