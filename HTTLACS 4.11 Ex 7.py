import turtle
wn = turtle.Screen()
abs = turtle.Turtle()

abs.up()
abs.goto(100,20),
abs.down()

list = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for i in list:
    abs.left(i)
    abs.forward(100)

print(abs.heading())

