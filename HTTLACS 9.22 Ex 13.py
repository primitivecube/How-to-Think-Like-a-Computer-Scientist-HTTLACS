# Here is another interesting L-System called a Hilbert curve. Use 90 degrees:

# L
# L -> +RF-LFL-FR+
# R -> -LF+RFR+FL-

# Note: somewhat confusingly, R and L do not translate as turtle instructions, but they are necessary for generating the
# recursive instructions. Only F,B, + and - are translated as turtle instructions (fwd, back, turn right, turn left).

import turtle

def createLSystem(numIters,axiom):
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
    if ch == 'L':
        newstr = '+RF-LFL-FR+'   # Rule 1
    elif ch == 'R':
        newstr = '-LF+RFR+FL-'
    else:
        newstr = ch    # no rules apply so keep the character

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
    inst = createLSystem(4, "L")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()
    # wn.tracer(0)

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 90, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()
