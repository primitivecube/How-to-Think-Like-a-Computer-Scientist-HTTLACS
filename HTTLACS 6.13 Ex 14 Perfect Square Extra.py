# Write a function called mySqrt that will approximate the square root of a number, call it n, by using Newton’s algorithm.
# Newton’s approach is an iterative guessing algorithm where the initial guess is n/2 and
# each subsequent guess is computed using the formula: newguess = (1/2) * (oldguess + (n/oldguess))

### I've changed it to return guess once the sqrt is perfect. It will fail to stop on recurring numbers, not sure how to fix that.

def perfect_mySqrt(n):
  guess = n / 2
  while n / guess != guess:
    newguess = (1/2) * (guess + (n/guess))
    guess = newguess
  return guess

print("%0.2f" % (perfect_mySqrt(100)))
