# X
# X --> F[-X]+X
# F --> FF

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
        newstr = 'F[-X]+X'   # Rule 1
    elif ch == 'Y':
        newstr = 'FF'
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
            loadState = saveState.pop()
            aTurtle.setheading(loadState[0])
            aTurtle.setposition(loadState[1], loadState[2])

def main():
    inst = createLSystem(7, "X")
    print(inst)
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.tracer(0)
    t.penup()
    t.setposition(0, -200)
    t.pendown()
    t.left(90)
    drawLsystem(t, inst, 30, 10)
    wn.exitonclick()

main()
