# Create a list containing 100 random integers between 0 and 1000 (use iteration, append, and the random module).
# Write a function called average that will take the list as a parameter and return the average.

import random

list1000 = []
for i in range (100):
    list1000.append(random.randint(0,1000))

def average (list):
    count = 0
    for number in list:
        count += number
    average = count / len(list)
    return average

print(average(list1000))

# Write a Python function that will take a the list of 100 random integers between 0 and 1000
# and return the maximum value.
# (Note: there is a builtin function named max but pretend you cannot use it.)

def maxValue (list):
    findMax = 0
    for number in list:
        if number > findMax:
            findMax = number
    return findMax

print(maxValue(list1000))
