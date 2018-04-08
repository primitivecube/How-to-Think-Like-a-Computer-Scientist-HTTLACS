import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
alex = turtle.Turtle()
alex.color("black")
alex.pensize(3)

def polygon_interior_angle(n):
    angle = (((n-2) * 180) / n)
    return angle

def interior_turtleturn(n):
    turn = 180 - (polygon_interior_angle(n))
    return turn

#print (polygon_interior_angle(10))

def drawpoly(someturtle, somesides, somesize):
    """Draw a uniform polygon by defining the turtle, number of sides, and size of each side"""
    for i in range (somesides):
        someturtle.forward(somesize)
        someturtle.left(interior_turtleturn(somesides))

def drawpoly_rotational_pattern(turtle, sides, size, pattern):
    """Draw a uniform polygon and repeat it with rotational symmetry by defining the turtle, number of sides, size of each sides, and number of rotations"""
    for count in range(pattern):
        drawpoly(turtle, sides, size)
        alex.left(interior_turtleturn(pattern))

drawpoly_rotational_pattern(alex, 4, 50, 20)

wn.exitonclick()
