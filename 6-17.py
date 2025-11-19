czas_24 = input('Podaj czas w formacie 24 godzinnym: ')
podzial = czas_24.split(':')
godzina = int(podzial[0])
minuta = int(podzial[1])

am_pm = '' #użyjemy tego do AM i PM
czas_12 = 0
if godzina < 12:
    am_pm = 'am'
else:
    am_pm = 'pm'

if godzina == 0: # północ 00:00 to 12:00AM
    czas_12 = 12
elif godzina == 12: # południe 12:00 to 12PM
    czas_12 = 12
elif godzina > 12:
    czas_12 = godzina - 12 # czyli np. godzina 14 to będzie 2PM (14-12=2)
else:
    czas_12 = godzina

print(f'Godzina w formacie 24 godzinnym to: {czas_24}')
print(f'Godzina w formacie 12 godzinnym to: {czas_12}:{minuta:02d}{am_pm}')                     