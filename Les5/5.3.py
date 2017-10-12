f = open('kaartnummers.txt', 'r')

smallestInt = 0

intList = [int(x.split(",")[0]) for x in f.readlines()]

regels = len(intList)
nummer = max(intList)
laatsteregel = ''

str_format = 'Deze file telt {0} regels\n' \
             'Het grootste kaartnummer is: {1} en dat staat op regel: 4'
result = str_format.format(regels, nummer, laatsteregel)
print(result)
