
import turtle
wn = turtle.Screen()

abs = turtle.Turtle()
abs.up()
abs.goto(-100,20)
abs.down()

list = [3,4,5,6]

def shape(t, sides, length, side_color, fill_color):
    t.color(side_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    for i in range (sides):
        t.forward(length)
        t.left(360 / sides)
    t.end_fill()

for i in list:
    shape(abs,i, 20, "red", "blue")
    abs.up()
    abs.forward(60)
    abs.down()


wn.exitonclick()

