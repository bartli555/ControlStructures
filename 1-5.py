###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
minimum_to_pass = total_tasks * 0.5
tasks_ok = 20
test_passed = False

if tasks_ok >= minimum_to_pass:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')