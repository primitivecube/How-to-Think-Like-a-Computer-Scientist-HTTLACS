
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

abs = turtle.Turtle()

abs.color("blue")
abs.shape("turtle")
abs.stamp()
abs.pensize(3)
abs.speed(0)
abs.hideturtle()
# wn.tracer(0,0)

def clock():
    for i in range(12):
        abs.up()
        abs.forward(90)
        abs.down()
        abs.forward(10)
        abs.up()
        abs.forward(10)
        abs.stamp()
        abs.forward(-110)
        abs.right(360 / 12)
        abs.down()

def clock_of_clocks():
    for i in range(12):
        abs.up()
        abs.forward(90)
        abs.down()
        abs.forward(10)
        abs.up()
        abs.forward(10)
        abs.stamp()
        clock()
        abs.up()
        abs.forward(-110)
        abs.right(360 / 12)
        abs.down()

clock_of_clocks()

wn.exitonclick()



