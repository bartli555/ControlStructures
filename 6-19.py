print('ANKIETA')
ankieta = input('Czy interesujesz się informatyką? (t/n)')
gry_kom = input('Czy lubisz grać w gry komputerowe? (t/n)')
insta = input('Czy masz konto na instagramie? (t/n)')

interesuje_sie_it = (ankieta == 't')
lubi_gry = (gry_kom == 't')
ma_instagrama = (insta == 't')

print('WYNIKI ANKIETY')
if interesuje_sie_it:
    print('Zainteresowanie informatyką: Tak')
else:
    print('Zainteresowanie informatyką: Nie')

if lubi_gry:
    print('Granie w gry komputerowe: Tak')
else:
    print('Granie w gry komputerowe: Nie')

if ma_instagrama:
    print('Posiadanie konta na Instagramie: Tak')
else:
    print('Posiadanie konta na Instagramie: Nie')             