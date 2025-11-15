###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus_amount = 0.0
bonus = 0.30 # 15%
is_bonus_input = input(f'Does the employee receive a bonus...? (Y/N):')
is_bonus = (is_bonus_input == 'Y')

if is_bonus:
    bonus_amount = basic_salary * bonus
    total_salary = basic_salary + bonus_amount
else:
    bonus_amount = 0
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')