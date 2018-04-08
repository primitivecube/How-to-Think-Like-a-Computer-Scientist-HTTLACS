import math

def is_rightangled(a, b, c):
    # your code here
    if abs(a**2 + b**2 - c**2) < 0.001:
        return True
    else:
        return False

print(is_rightangled(3,4,5))
