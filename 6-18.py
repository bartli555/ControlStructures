x_str = input('Podaj liczbę x: ')
y_str = input('Podaj liczbę y: ')
x = int(x_str)
y = int(y_str)

if x > 0 and y > 0:
    print(f'Punkt P ({x},{y}) znajduje się w pierwszej ćwiartce')
elif x < 0 and y > 0:
    print(f'Punkt P ({x},{y}) znajduje się w drugiej ćwiartce')    
elif x < 0 and y < 0:
    print(f'Punkt P ({x},{y}) znajduje się w trzeciej ćwiartce') 
elif x > 0 and y < 0:
    print(f'Punkt P ({x},{y}) znajduje się w czwartej ćwiartce')
elif x == 0 and y == 0:
    print(f'Punkt P ({x},{y}) znajduje się w położeniu (0,0)')
elif x == 0:
    print(f'Punkt P ({x},{y}) leży na osi Y')
elif y == 0:
    print(f'Punkt P ({x},{y}) leży na osi X')               