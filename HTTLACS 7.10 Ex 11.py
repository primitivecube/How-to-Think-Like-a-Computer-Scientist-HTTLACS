import math

def is_rightangled(a, b, c):
    # your code here
    if c > b and c > a:
        return abs(a**2 + b**2 - c**2) < 0.001
    elif b > c and b > a:
        return abs(a**2 + c**2 - b**2) < 0.001
    elif a > b and a > c:
        return abs(b**2 + c**2 - a**2) < 0.001
    else:
        return False

print(is_rightangled(3,4,5))
