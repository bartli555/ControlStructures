aktualna_cena = 140.00
poprzednia_cena = 200.00

if aktualna_cena < poprzednia_cena:
    obnizka_kwota = poprzednia_cena - aktualna_cena
    obnizka_procent = (obnizka_kwota / poprzednia_cena) * 100
if obnizka_procent >= 10:
    print(f'Aktualna cena produktu: {aktualna_cena:.2f}')
    print(f'Poprzednia cena produktu: {poprzednia_cena:.2f}')
    print('Kup produkt!!')
    print(f'Cena produktu obniżona o: {obnizka_procent:g}%')    