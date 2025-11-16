###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

not_zero = (x >= 0) or (y >= 0)

if not_zero:
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    print('Obie cyfry są ujemne')    