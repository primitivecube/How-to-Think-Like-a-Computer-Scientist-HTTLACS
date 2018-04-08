# Extend the star function to draw an n pointed star.
# (Hint: n must be an odd number greater or equal to 3).

import turtle

alex = turtle.Turtle()
alexa = turtle.Turtle()

wn = turtle.Screen()

# wn.bgcolor("light green")

# alex.color("pink")

alex.pensize(5)
alexa.pensize(5)

def drawFivePointStar(t):
    for i in range(5):
        t.forward(100)
        t.right(144)

def drawFiveStars(t):
    for i in range (5):
        drawFivePointStar(t)
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()

def star_turn_angle(n):
    angle = 180 - (180 / n)
    return angle

def draw_n_pointed_star(t, n):
    """Draw a star with n points, given a turtle [t] and number of points [n]. Stars must have an odd number of points,
     even-integer arguments will be converted to the next highest odd integer"""
    if n % 2 != 1:
        n += 1
    for i in range (n):
        t.forward(100)
        t.right(star_turn_angle(n))

# alex.penup()
# alex.left(180)
# alex.forward(200)
# alex.left(180)
# alex.pendown()

# drawFivePointStar(alex)

# drawFiveStars(alex)

draw_n_pointed_star(alex, 7)

wn.exitonclick()
