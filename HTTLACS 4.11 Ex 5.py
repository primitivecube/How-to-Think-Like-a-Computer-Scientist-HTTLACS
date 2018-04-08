import turtle
wn = turtle.Screen()

abs = turtle.Turtle()
abs.up()
abs.goto(-100,20)
abs.down()

def shape(t, sides):
    for i in range (sides):
        t.forward(20)
        t.left(360 / sides)

for i in (3,4,6,8):
    shape(abs,i)
    abs.up()
    abs.forward(60)
    abs.down()




wn.exitonclick()
