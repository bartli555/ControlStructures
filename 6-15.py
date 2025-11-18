ean_number = input('Wprowadź numer EAN: ')
if len(ean_number) == 13:
    print('Numer EAN jest poprawny')

    if ean_number[0:3] == '590':
        print('Artykuł Made in Poland')

else:
    print('Numer jest niepoprwany(musi mieć 13 cyfr)')
