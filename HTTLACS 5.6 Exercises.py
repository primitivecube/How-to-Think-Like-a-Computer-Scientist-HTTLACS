import random
import math

# Use a for statement to print 10 random numbers.

for i in range(10):
    print (i, random.random())

# Repeat the above exercise but this time print 10 random numbers between 25 and 35, inclusive.

for i in range(10):
    print (i, random.randrange(25,36))

# The Pythagorean Theorem tells us that the length of the hypotenuse of a right triangle
# is related to the lengths of the other two sides. Look through the math module and see if
# you can find a function that will compute this relationship for you.
# Once you find it, write a short program to try it out.

print(math.hypot(3,4)) # prints the hypotenuse in a x = 3, y = 4 triangle

# Search on the internet for a way to calculate an approximation for pi. There are many that use simple arithmetic.
# Write a program to compute the approximation and then print that value as well as the value of math.pi from the math module.

# The Euler approximation of pi: pi = 20 x arctan (1 / 7) + (8 x arctan (3 / 79))

pi = 20 * math.atan(1 / 7) + (8 * math.atan(3 / 79))

print(pi)
