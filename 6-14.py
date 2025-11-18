facebook = False
twitter = True
instagram = True

print(f"facebook = {'prawda' if facebook else 'fałsz'}")
print(f"twitter = {'prawda' if twitter else 'fałsz'}")
print(f"instagram = {'prawda' if instagram else 'fałsz'}")

liczba_kont = facebook + twitter + instagram

if liczba_kont >= 2:
    print("Jesteś dobrym influencerem!")
else:
    print('Nie jesteś dobrym influencerem :(')    