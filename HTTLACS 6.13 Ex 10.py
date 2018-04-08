# Extend your program above. Draw five stars, but between each,
# pick up the pen, move forward by 350 units, turn right by 144,
# put the pen down, and draw the next star. You’ll get something like this
# (note that you will need to move to the left before drawing your first star in order to fit everything in the window):

import turtle

alex = turtle.Turtle()

wn = turtle.Screen()
wn.bgcolor("light green")

alex.color("pink")
alex.pensize(5)

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

alex.penup()
alex.left(180)
alex.forward(200)
alex.left(180)
alex.pendown()

#drawFivePointStar(alex)

drawFiveStars(alex)

wn.exitonclick()
