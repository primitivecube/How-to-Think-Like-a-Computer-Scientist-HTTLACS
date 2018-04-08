# Write a function called fancySquare that will draw a square with fancy corners (sprites on the corners).
# You should implement and use the drawSprite function from above.
# For an even more interesting look, how about adding small triangles to the ends of the sprite legs.

import turtle

alex = turtle.Turtle()
wn = turtle.Screen()

# def drawSprite(turtle, legs, length):
#     for i in range (4):
#         turtle.forward(length * legs)
#         turtle.left(90)
#     for i in range (legs):
#         for i in range (3):
#             turtle.forward(length)
#             turtle.right(120)
#         turtle.forward(length)
#
#
# drawSprite(alex, 4, 30)
#

def drawSprite(turtle, legs, length):
    angle = (360 / legs)
    for i in range (legs):
        turtle.forward(length)
        turtle.backward(length)
        turtle.right(angle)

# drawSprite(alex,15,120)

def drawFancySquare(turtle,legs,length):
    for i in range (4):
        drawSprite(turtle, legs, length)
        turtle.forward(length * 4)
        turtle.right(90)

# drawFancySquare(alex, 8, 10)

def drawMoreFancySquare(turtle, legs, length):
    angle = (360 / legs)
    for i in range (4):
        for i in range (legs):
            turtle.forward(length)
            for i in range (3):
                turtle.forward(length / 3)
                turtle.right(120)
            turtle.backward(length)
            turtle.right(angle)
        turtle.forward(length * 4)
        turtle.right(90)

drawMoreFancySquare(alex,8,10)

wn.exitonclick()


