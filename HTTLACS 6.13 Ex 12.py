
# Write a function called drawSprite that will draw a sprite. T
# the function will need parameters for the turtle, the number of legs, and the length of the legs.
# Invoke the function to create a sprite with 15 legs of length 120.


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

drawSprite(alex,15,120)

wn.exitonclick()


