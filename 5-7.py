###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:

    if countdown == 5:
        print('pięć')
    elif countdown == 4:
        print('cztery')
    elif countdown == 3:
        print('trzy')
    elif countdown == 2:
        print('dwa')
    elif countdown == 1:
        print('jeden')                
    else:
        print(countdown)
    countdown -= 1
    time.sleep(1)  # Wait for 1 second   

print("Time's up!")