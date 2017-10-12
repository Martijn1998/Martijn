file = open('hardlopers.txt', 'w')
tl = (import datetime)
tl.strftime('%y/%m/%d %H:%M:%S', tl)
file.write(tl.strftime('%a %d %b %Y, %H:%M:%S', tl)+ ', '+input('hardloper: ' + '\n'))
file.close()

file = open('hardlopers.txt', 'r')
print(file.read())
