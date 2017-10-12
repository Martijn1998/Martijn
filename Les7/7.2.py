invoer = ''

while len(invoer) != 4:
    invoer = (input('Geef een string van vier letters:'))
    if len(invoer) != 4:
        print('{} heeft {} letter.'.format(invoer, len(invoer)))
    else:
        print('Inlezen van correcte string: {} drop is geslaagd'.format(invoer))