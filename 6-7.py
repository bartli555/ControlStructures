wiek = int(input('Podaj wiek użytkownika: '))

if wiek < 13:
    print('Jesteś dzieckiem')
elif wiek <= 19:
    print('Jesteś nastolatkiem')
elif wiek < 65:
    print('Jesteś dorosły')
elif wiek >= 65:
    print('Jesteś seniorem')            
