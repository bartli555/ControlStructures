PIN = '0805'
max_prob = 3

for proba in range(max_prob):
    wprowadzany_pin = input('Wprowadź KOD PIN: ')

    if wprowadzany_pin == PIN:
        print('Wprowadzony PIN jest poprawny.')
        break
    else:
        print('PIN Nieprawidłowy')    

else:
    print('Niestety, Twoja karta płatnicza została zablokowana.')