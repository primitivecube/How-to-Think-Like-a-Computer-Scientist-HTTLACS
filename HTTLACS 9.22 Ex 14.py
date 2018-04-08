# Here is a dragon curve. Use 90 degrees.:
# FX
# X -> X+YF+
# Y -> -FX-Y

# This program requires a high number of iterations to see the dragon curve
# take shape, at least 10

import turtle

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'X':
        newstr = 'X+YF+'   # Rule 1
    elif ch == 'Y':
        newstr = '-FX-Y'
    else:
        newstr = ch     # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLSystem(10, "FX")  # create the string
    print(inst)
    t = turtle.Turtle()           # create the turtle
    wn = turtle.Screen()
    wn.tracer(0)

    t.up()
    t.back(100)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 90, 5)   # draw the picture
                                  # angle 90, segment length 5
    wn.exitonclick()

main()
