#Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and including n.
#So sumTo(10) would be 1+2+3...+10 which would return the value 55.
#Use the equation (n * (n + 1)) / 2.

def sumTo(n):
    equation = (n * (n + 1)) / 2
    return equation

def alt_sumTo(n):
    equation = 0
    for i in range(n+1):
        equation += i
    return equation

print("Result of sum:", sumTo(123))

print("Result of alt_sum:", alt_sumTo(123))
