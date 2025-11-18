godziny_parkowania = int(input('Podaj liczbę godzin parkowania: '))

if godziny_parkowania <= 2:
    print('Opłata wynośi 5zł')
elif godziny_parkowania <= 6:
    print('Opłata wybosi 15zł')
elif godziny_parkowania > 6:
    print('Opłata wynosi 20zł')        
