# Here are the rules for an L-system that creates something that resembles a common garden herb.
# Implement the following rules and try it. Use an angle of 25.7 degrees.
# H
# H --> HFX[+H][-H]
# X --> X[-FFF][+FFF]FX

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
    if ch == 'H':
        newstr = 'HFX[+H][-H]'   # Rule 1
    elif ch == 'X':
        newstr = 'X[-FFF][+FFF]FX' # Rule 2
    else:
        newstr = ch     # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    saveState = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
                saveState.append([aTurtle.heading(),aTurtle.xcor(),aTurtle.ycor()])
        elif cmd == ']':
            if len(saveState) > 0:
                loadState = saveState.pop()
                aTurtle.setheading(loadState[0])
                aTurtle.setposition(loadState[1], loadState[2])

def main():
    inst = createLSystem(3, "H") # the first item is iterations, the second is the axiom
    print(inst)
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.setposition(0, 0)
    t.pendown()
    t.left(30)
    drawLsystem(t, inst, 25.7, 5) # angle is the third item here, the fourth item is length

main()
