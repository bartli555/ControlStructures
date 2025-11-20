liczba_str = input('Wprowadź liczbę od 1 do 10: ')
liczba = int(liczba_str)

for i in range(1,11):
    wynik = liczba * i
    print(f'{liczba} * {i} = {wynik}')