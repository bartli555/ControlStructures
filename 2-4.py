###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = input('Podaj pierwszą liczbę: ')
num1 = int(number1)
number2 = input('Podaj drugą liczbę: ')
num2 = int(number2)
operator = input('Podaj operator działania: ')

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2    

# print result
print(f'{num1} {operator} {num2} = {result}')