def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0
    while n != 1:
        count += 1
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    return count

def seq3np1_iter(start,limit):
    seq3np1_iterations = []
    for i in range (start, limit+1):
        seq3np1_iterations.append(seq3np1(i))
    return seq3np1_iterations

import turtle
wn = turtle.Screen()
wn.tracer(0)

tess = turtle.Turtle()

# tess.speed(0)

def drawBar(t, height, start):
    """ Get turtle t to draw one bar, of height. """
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()

    condition = height > 100

    if condition:
        t.right(90)
        t.backward(height)
        t.left(90)
        t.backward(10)
        t.left(90)
        t.forward(10)
        t.write("{0}, {1}".format(start, height))
        t.backward(10)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(height)
        t.left(90)

def barChart(t, start, limit):

    llx = (len(seq3np1_iter(start,limit)) * 10 + 10) * -1
    urx = (len(seq3np1_iter(start,limit)) * 10 + 10)
    lly = (max(seq3np1_iter(start,limit)) + 10) * -1
    ury = (max(seq3np1_iter(start,limit)) + 10)
    wn.setworldcoordinates(llx,lly,urx,ury)
    t.penup()
    t.setpos((llx // 2),(lly // 2))
    t.pendown()
    t.color("blue")
    t.fillcolor("red")

    for i in range(start, limit):
        drawBar(t, seq3np1(i), i)

barChart(tess,1,50)

wn.exitonclick()
