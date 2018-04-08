# Write a function called myPi that will return an approximation of PI (3.14159…).
# Use the Madhava approximation.
# Madhava approximation: pi = math.sqrt(12) * (1-(1 / (3 * (3 ** 1) + (1 / (5 * (3 ** 2) - (1 / (7 * (3 ** 3)...))))
# pi = math.sqrt(12) * (1-pattern)
# add_sub = 1
# power = 1
# denominator = 3.3
# pattern = 1 / denominator ** power # accumulating series

import math

def madhava_pi(iter):
    add_sub = 1
    power = 1
    denominator = 3
    pattern = 0
    for i in range(iter):
        pattern += add_sub * (1 / (denominator * (3 ** power)))
        add_sub = add_sub * -1
        denominator += 2
        power += 1
    pi = math.sqrt(12) * (1-pattern)
    return pi

print(madhava_pi(100))
