a = 0
b = 1

print(a, end=' ')
print(b, end=' ')

for i in range(18):
    kolejny_wyraz = a + b #kolejny wyraz to suma dwóch poprzednich
    print(kolejny_wyraz, end=' ') #printujemy kolejny obliczony wyraz, kończymy spacją

    a = b #przesuwamy liczby "w lewo"  czyli a przyjmuje wartośc b
    b = kolejny_wyraz #b przyjmuje wartośc kolejnego, żeby to wszystko działało jak ciąg czyli każdy kolejny wyraz jest sumą dwóch poprzednich