# Concepts: Random module, Loops, Conditions

import random

while True:
    print('1. Roll Dice\n2. Exit')
    user = int(input('Enter your choice: '))

    if user == 1:
        number = random.randint(1,6)
        print(number)

    else:
        break