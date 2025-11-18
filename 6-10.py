wiek_rzeczywisty = float(input('Podaj wiek psa (w latach ludzkich): '))
if wiek_rzeczywisty <= 2:
    psie_lata = wiek_rzeczywisty * 10.5
else:
    pierwsze_dwa_lata = 21
    pozostale_lata = wiek_rzeczywisty - 2
    psie_lata = pierwsze_dwa_lata + (pozostale_lata * 4)

print(f'Wiek psa w latach ludzkich wynosi: {wiek_rzeczywisty:g}')
print(f'Wiek psa w latach psich wynosi: {psie_lata:g}')
