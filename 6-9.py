imie = input('Podaj imie: ')
ostatnia_litera = imie[-1]

if ostatnia_litera == 'a':
    print(f'{imie} -- polskie imię żeńskie')
else:
    print('To prawdopodobnie imię męskie')    