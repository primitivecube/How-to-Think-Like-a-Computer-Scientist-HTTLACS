# There was a whole program in A Turtle Bar Chart to create a bar chart with specific data.
# Creating a bar chart is a useful idea in general. Write a non-fruitful function called barChart,
# that takes the numeric list of data as a parameter, and draws the bar chart. Write a full program calling this function.
# The current version of the drawBar function unfortuately draws the top of the bar through the bottom of the label.
# A nice elaboration is to make the label appear completely above the top line.
# To keep the spacing consistent you might pass an extra parameter to drawBar for the distance to move up.
# For the barChart function make that parameter be some small fraction of maxheight+border.
# The fill action makes this modification particularly tricky:
# You will want to move past the top of the bar and write before or after drawing and filling the bar.

import turtle

def drawBar(t, height, pensize):
    """ Get turtle t to draw one bar, of height. """
    t.pensize(pensize)
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    #t.write(str(height))
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape
    t.penup()
    t.right(90)
    t.backward(height)
    #t.write(str(height))
    t.left(90)
    #t.write((str(height)))
    t.backward(10)
    t.left(90)
    t.forward((maxheight+border / 100))
    t.write(str(height), font=("Arial", 20, "normal"))
    t.backward((maxheight+border / 100))
    t.right(90)
    t.left(90)
    t.backward(height)
    t.right(90)
    t.forward(10)
    t.pendown()


xs = [1,2,3]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()             # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")
wn.tracer(0)

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
#tess.pensize(3)

#
#
# for a in xs:
#     drawBar(tess, a)
#

#
def barChart(turtle, list, pensize):
    for a in list:
        drawBar(turtle, a, pensize)

barChart(tess,xs, 1)

wn.exitonclick()
