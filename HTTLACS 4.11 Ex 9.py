import turtle
wn = turtle.Screen()
abs = turtle.Turtle()

def star(t, points):
    angle = (180 - 180 / points)
    for i in range(points):
        t.forward(100)
        t.right(angle)

star(abs, 5)

