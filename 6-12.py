ilosc = int(input('Podaj liczbę zakupionych produków: '))
cena = float(input('Podaj cenę produktu: '))
kwota_do_zaplaty = 0.0

if ilosc <= 2:
    kwota_do_zaplaty = ilosc * cena
else:

    pelna_kwota = 2 * cena

    ilosc_z_rabatem = ilosc - 2
    cena_z_rabatem = cena * 0.75
    kwota_z_rabatem = cena_z_rabatem * ilosc_z_rabatem

    kwota_do_zaplaty = pelna_kwota + kwota_z_rabatem

print(f'Ilość zakupionych produktów: {ilosc}')
print(f'Cena za produkt: {cena:g}')
print(f'Kwota do zapłaty to: {kwota_do_zaplaty:.2f}')
