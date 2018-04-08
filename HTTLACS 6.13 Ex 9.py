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

def draw_spiral(turtle, length, turns, angle):
    """Draw a spiral by defining a turtle, initial length, number of turns, and turn angle"""
    for count in range(turns):
        turtle.forward(length)
        turtle.right(angle)
        length += 3

alex.penup()
alex.right(90)
alex.pendown()

#draw_spiral(alex, 5, 20, 90) # square spiral

def drawSpiral(t, angle):
    ''' takes a turtle, t, and an angle in degrees '''
    length = 1
    for i in range(84):
        t.forward(length)
        t.right(angle)
        length = length + 2

# draw_spiral(alex, 5, 20, 89) # not quite square spiral

#Write a non-fruitful function drawEquitriangle(someturtle, somesize) which calls drawPoly
#from the previous question to have its turtle draw a equilateral triangle.

def drawEquitriangle(someturtle, somesize):
    """Draw an equiliateral triangle by providing and turtle and the size of the sides"""
    drawpoly(someturtle, 3, somesize)

# drawEquitriangle(alex, 20)

#Write a non-fruitful function to draw a five pointed star, where the length of each side is 100 units.

def five_pointed_star_drawpoly(someturtle):
    for i in range (5):
        someturtle.forward(100)
        someturtle.left(144)

alex.penup()
alex.right(90)
alex.pendown()

five_pointed_star_drawpoly(alex)

wn.exitonclick()
