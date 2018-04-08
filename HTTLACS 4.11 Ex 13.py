
import turtle
wn = turtle.Screen()
abs = turtle.Turtle()
abs.speed(0)

def sprite(n):
    for i in range (n):
        abs.forward(100)
        abs.forward(-100)
        abs.right(360 / n)

sprite(40)

wn.exitonclick()

