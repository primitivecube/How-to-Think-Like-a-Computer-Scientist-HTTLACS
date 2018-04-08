# Write a function called mySqrt that will approximate the square root of a number, call it n, by using Newton’s algorithm.
# Newton’s approach is an iterative guessing algorithm where the initial guess is n/2 and
# each subsequent guess is computed using the formula: newguess = (1/2) * (oldguess + (n/oldguess))

def mySqrt(n, guesses):
  oldguess = n / 2
  for i in range(guesses):
    newguess = (1/2) * (oldguess + (n/oldguess))
    oldguess = newguess
  return newguess

print(mySqrt(9,6))
