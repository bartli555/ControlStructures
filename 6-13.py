predkosc_samochodu = int(input('Wprowadz predkosc samochodu: '))
limit_prędkości_mix = 40.00
limit_prędkoćci_max = 140.00

if predkosc_samochodu < 40:
    print('Nieprawidłowa prędkośc samochodu')
elif predkosc_samochodu > 140:
    print('Nieprawidłowa prędkość samochodu')
else:
    print('Prędkość jest prawidłowa')            