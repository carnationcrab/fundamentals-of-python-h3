# SAM MARTORANA

# ################################# [H3_1] ################################# #
# Write a program that prints out 100 random integers, each in the range 1
# through 6.
# ########################################################################## #

import random

def printRandomIntegers():
    for i in range(100):
        print('integer', i + 1, ':', random.randint(1, 6))


printRandomIntegers()
