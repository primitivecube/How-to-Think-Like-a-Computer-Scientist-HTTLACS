#Write a function areaOfCircle(r) which returns the area of a circle of radius r.
#Make sure you use the math module in your solution.

import math

def areaOfCircle(r):
    """Return the area of a circle of radius r"""
    area = math.pi * (r**2)
    return area

print("The area of the circle is:", areaOfCircle(1.2))

