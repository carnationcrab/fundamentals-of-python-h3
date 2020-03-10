# SAM MARTORANA

# ################################# [H3_2] ################################# #
# Write a program that reads an int numRolls from the user, then generates
# numRolls random integers, each in the range 1 through 6. This simulates
# rolling a single fair (unbiased) die.
#
# Use a for-loop and the accumulator pattern to add together the values of
# these rolls in the integer variable sum, then compute the average roll
# value (sum / numRolls).  Print out this average.  What do you expect for
# this average, as numRolls gets larger and larger? 
# ########################################################################## #

import random

numRolls = int(input('Give us the number of rolls please: '))

def roll(numOfTimes):
    total = 0
    for i in range(numOfTimes):
        total += random.randint(1, 6)
    print('Your average roll is', (total / numOfTimes))


roll(numRolls)

# Average should get closer to 3 the more rolls you do, right?
