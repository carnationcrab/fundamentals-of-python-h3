# SAM MARTORANA

# ################################# [H3_3] ################################# #
# Here's another way of approximating Pi, using the Madhava-Leibniz formula:
#
# Pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...
#
# Notice how the signs alternate between + and - for each term of this
# series (1, -1/3, 1/5, -1/7, etc.). Write a program which reads num_terms
# as an int, then computes the above approximation of Pi/4 by summing the
# first num_terms terms of this series.  Then multiply your computed sum by
# 4 and print out the resulting approximate calculated value of Pi as well
# the error: the absolute value of its difference with math.pi.  
#
# Hint: use a loop with header for count in range(num_terms), after you
# initialize a float accumulator pi_estimate to 0.0 and sign to 1.0.
# Your indented loop body should first calculate
# term = sign / (2*count + 1), then add term to your pi_estimate accumulator.
# The final statement within your loop body should be sign = -sign so that
# the term calculated in the next iteration of the for-loop will have the
# opposite sign. After the loop ends, calculate and print 4*pi_estimate and
# its absolute value difference from math.pi:  abs(math.pi-4*pi_estimate).
# ########################################################################## #

import math

num_terms = int(input('Give us num_terms, please: '))

pi_estimate = 0.0
sign = 1.0

for i in range(num_terms):
    term = sign / (2 * i + 1)
    pi_estimate += term
    sign = (-sign)

bestGuess = 4 * pi_estimate

result = abs(math.pi - bestGuess)

print(result)
