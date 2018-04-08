import random
import turtle

def moveRandom(wn, t):
    coin = random.randrange(0,2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

def areColliding(t1, t2):
    if t1.distance(t2) < 2:
        return True
    else:
        return False

def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False
    return stillIn

t1 = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()

t1.shape('turtle')
t2.shape('circle')
t1.speed(0)
t2.speed(0)

leftBound = -wn.window_width() / 2
rightBound = wn.window_width() / 2
topBound = int(wn.window_height() / 2)
bottomBound = int(-wn.window_height() / 2)

print(topBound, bottomBound)

t1.up()
t1.goto(0.5 * random.randint(leftBound,rightBound),0.5 * random.randint(bottomBound,topBound))
t1.setheading(random.randrange(0, 360))
t1.down()

t2.up()
t2.goto(0.5 * random.randint(leftBound,rightBound),0.5 * random.randint(bottomBound,topBound))
t2.setheading(random.randrange(0, 360))
t2.down()


while isInScreen(wn, t1) and isInScreen(wn, t2):
    moveRandom(wn, t1)
    moveRandom(wn, t2)
    if areColliding(t1,t2):
        t1.left(180)
        t2.left(180)
        t1.forward(20)
        t2.forward(20)

if not isInScreen(wn, t1):
    t1.left(180)
    t1.forward(100)
    while isInScreen(wn, t1) and isInScreen(wn, t2):
        moveRandom(wn, t1)
        moveRandom(wn, t2)
        if areColliding(t1,t2):
            t1.left(180)
            t2.left(180)
            t1.forward(20)
            t2.forward(20)

if not isInScreen(wn, t2):
    t2.left(180)
    t2.forward(100)
    while isInScreen(wn, t1) and isInScreen(wn, t2):
        moveRandom(wn, t1)
        moveRandom(wn, t2)
        if areColliding(t1,t2):
            t1.left(180)
            t2.left(180)
            t1.forward(20)
            t2.forward(20)

wn.exitonclick()

