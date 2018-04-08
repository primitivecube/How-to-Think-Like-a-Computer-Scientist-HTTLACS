#Write a non-fruitful function drawPoly(someturtle, somesides, somesize)
#which makes a turtle draw a regular polygon.
#When called with drawPoly(tess, 8, 50), it will draw a shape like this

import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
alex = turtle.Turtle()
alex.color("black")
alex.pensize(3)

def polygon_interior_angle(n):
    angle = (((n-2) * 180) / n)
    return angle

def interior_turtleturn(n):
    turn = 180 - (polygon_interior_angle(n))
    return turn

#print (polygon_interior_angle(10))

def drawpoly(someturtle, somesides, somesize):
    """Draw a uniform polygon by defining the turtle, number of sides, and size of each side"""
    for i in range (somesides):
        someturtle.forward(somesize)
        someturtle.left(interior_turtleturn(somesides))

drawpoly(alex, 8, 50)

wn.exitonclick()
