
import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("blue")

alex = turtle.Turtle()
alex.color("black")
alex.pensize(3)

xy = 20
for count in range(5):
    drawSquare(alex,xy)
    alex.penup()
    alex.forward(xy*2)
    alex.pendown()

wn.exitonclick()

