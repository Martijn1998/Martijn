def convert(celcius):
    fahrenheit = celcius * 1.8+32
    return fahrenheit

def table():

    print('   F     C')
    for celcius in range(-30, 40, 10):
        fahrenheit = convert (celcius)
        print('{0:5} {1:5}'.format(fahrenheit, celcius))


(table())