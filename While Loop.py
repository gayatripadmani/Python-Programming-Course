## While Loop ##

# While loop is used to repeat a selection of code unknown number of times until a specific condition is met.

# while Expressions:
#      statement(s)

# i = 1
# while i <= 10:
#     print("Simplilearn")
#     i += 1

import random

nump = random.randint(1000, 9999)
n = int(input("Enter any four digit numbers: "))

while n != 10:
    num = nump
    cor = 0

    while num % 10:
        numc = num % 10
        num = num // 10
        nc = n // 10

        if numc == nc:
            cor = cor + 1

    if cor == 4:
        print("Congrates! you guessed it right")
        break

    else:
        print("%d digits were guessed right")
        n = int(input("Enter any four digit numbers: "))

else:
    print("You quit the game..!")