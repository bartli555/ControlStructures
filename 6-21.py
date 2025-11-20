kwota_str = input('Podaj kwotę w monetach: ')
kwota = int(kwota_str)

if kwota > 0:
    
    piątki = kwota // 5 #ile całych piątek zmieści się w kwocie
    reszta = kwota % 5 #reszta z dzielenia

    dwójki = reszta // 2 #ile całych dwójek zmieści się w kwocie
    reszta = reszta % 2 #reszta

    jedynki = reszta

    print(f'Kwota {kwota} w monetach: ')
    print(f'5 złoty monety: {piątki}')
    print(f'2 złote monety: {dwójki}')
    print(f'1 złoty monety: {jedynki}')    