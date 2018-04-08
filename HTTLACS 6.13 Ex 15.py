# Write a function called myPi that will return an approximation of PI (3.14159...).
# Use the Leibniz approximation: 1 - 1/3 + 1/5 - 1/7 + 1/9 ... = pi/4

def liebniz_pi(iter):
  accum = 0
  pos_neg = 1
  denominator = 3
  for i in range (iter):
    accum += pos_neg * (1 / denominator)
    denominator += 2
    pos_neg = pos_neg * -1
  sum = 1 - accum
  pi = 4 * sum
  return pi

print(liebniz_pi(10000))
