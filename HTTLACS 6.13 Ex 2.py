
import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
alex = turtle.Turtle()
alex.color("black")
alex.pensize(3)

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def drawSquares(number_of_squares, square_size):
    for count in range(number_of_squares):
        drawSquare(alex, square_size)
        alex.penup()
        alex.left(180)
        alex.forward(10)
        alex.left(90)
        alex.forward(10)
        alex.left(90)
        alex.pendown()
        square_size = square_size + 20

drawSquares(2, 20)

wn.exitonclick()

