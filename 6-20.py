liczba_str = input("Wprowadź liczbę dziesiętną: ")
liczba_dziesietna = int(liczba_str)

oryginalna_liczba = liczba_dziesietna

reszty = []

while liczba_dziesietna > 0:
    reszta = liczba_dziesietna % 2
    reszty.append(reszta)

    liczba_dziesietna = liczba_dziesietna // 2

reszty.reverse()
liczba_binarna = "".join(map(str, reszty))   

print(f'{oryginalna_liczba}(10) = {liczba_binarna}(2)')