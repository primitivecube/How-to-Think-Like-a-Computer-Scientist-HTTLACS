# Rewrite the function sumTo(n) that returns the sum of all integer numbers up to and including n. \
# This time use the accumulator pattern.

def sumTo(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

print(sumTo(10))
