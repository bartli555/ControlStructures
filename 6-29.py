liczba_naturalna_str = input('Podaj ile liczb naturalnych chcesz znaleźć: ')
liczba_naturalna = int(liczba_naturalna_str)

if liczba_naturalna > 0:
    znalezione = 0
    kandydat = 2
    
    while znalezione < liczba_naturalna:
        
        jest_pierwsza = True
        for dzielnik in range(2, kandydat):
            if kandydat % dzielnik == 0:
                jest_pierwsza = False
                break

        if jest_pierwsza:
            print(kandydat, end=' ')
            znalezione += 1

        kandydat += 1
    print()
