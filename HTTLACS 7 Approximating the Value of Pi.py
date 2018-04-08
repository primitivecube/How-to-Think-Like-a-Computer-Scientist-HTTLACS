import turtle
import random

fred = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)
wn.tracer(0)

fred.up()

numdarts = 1000 # a higher number of darts will give a closer approximation to pi, this is explained in the following comments

insideCount = 0

for i in range(numdarts): # the numdarts will represent the area of a square, due to the equal properties of randx and randy

    randx = (random.randrange(-100,100)) / 100
    randy = (random.randrange(-100,100)) / 100

    fred.goto(randx, randy) # This causes the "dart" to "land" somewhere inside a square

    if fred.distance(0,0) <= 1: # this checks if the "dart" lands in the "circle", because a fixed distance from origin
                                # represents a radius, and therefore marks out a circle.
        insideCount += 1
        fred.color("red")
        fred.dot()
    else:                       # This checks if the dart is outside the area of the circle, but within the area of the square
        fred.color("blue")      # Note that indsideCount is not incremented in this case
        fred.dot()

print((insideCount / numdarts) * 4) # This will approximate pi, see the logic below:

# So, why does the print statement approximate pi? Let's start with the formula for pi, then relate it to a square:
# pi = circumference of a circle / 2 * radius
# And to rearrange the print formula...
# ~pi = (insideCount / numbdarts) * 4
# The maximum range of the darts represents the area of a square
# A lesser range of the darts is within a circle, the sides of which meet the edges of the square (the "inscribing square")
# Where a circle is inscribed by a square, the diameter of the circle is equal to the length of a side of the square,
# therefore, if the radius or length of a side is known, then all properties of the square and circle can be determined
# using pi. The forumla is as follows:
# area of a circle / area of an inscribing square = pi / 4 # Or, expressed in properties of a circle:
# pi * (radius pow 2) / (radius * 2) pow 2 = pi / 4
# We know that the insideCount represents the area of a circle, and the numdarts represents the area of an inscribing square
# Let's rearrange the print statement to investigate the values of insideCount and numdarts:
# insideCount / numdarts = 3.14 / 4
# insideCount / numdarts = 0.785 # let's try substituting insideCount for area of the circle,
# and numdarts for the area of the inscribing square:
# pi*(radius pow 2) / (radius * 2) pow 2 = pi / 4 # Let's test some radii in that formula:
# 3.14 * (5 ** 2) / (5 * 2) ** 2 = 0.785
# 3.14 * (9 ** 2) / (9 * 2) ** 2 = 0.785 = pi / 4 # Great, looks like the formula works, now we can see how it rearranges into
# the print statement from our program, by multiplying each side by 4:
# pi = (pi * (radius ** 2) / (radius * 2) ** 2) * 4
# And to express all the formulas we've covered...
# pi = 3.14 = (insideCount / numdarts) * 4 = (A(circle) / A(inscribing square)) * 4 = (pi * (radius ** 2) / (radius * 2) ** 2) * 4

# Thank you @winterforge for assisting with this program

wn.exitonclick()

