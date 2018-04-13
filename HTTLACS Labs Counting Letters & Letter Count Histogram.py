# Define the function to require one parameter, the string.
# Create an empty dictionary of counts.
# Iterate through the characters of the string, one character at a time.

def countAll(forString):
    dict = {}
    for i in forString:
        dict[i] = 0
    for i in forString:
        dict[i] += 1
    return dict

print(countAll('banana'))

# The previous lab wrote a function to return a dictionary of letter counts.
# In an earlier chapter, we wrote a turtle program that could draw a histogram.
#
# Combine these two ideas together to create a function that will take a string and
# create a histogram of the number of times each letter occurs. Make sure it is in alphabetical order from left to right.
#
# Count the number of times each letter occurs. Keep the count in a dictionary.
# Get the keys from the dictionary, convert them to a list, and sort them.
# Iterate through the keys, in alphabetical order, getting the associated value (count).
# Make a histogram bar for each.

import turtle

def countAndDraw(forString):

    dict = {}

    for i in forString:
        dict[i] = 0

    for i in forString:
        dict[i] += 1

    keyList = list(dict)
    keyList.sort()
    turtleHeightList = []

    for i in keyList:
        turtleHeightList.append(dict.get(i))

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(0,0,len(keyList)*100,max(turtleHeightList)*100)

    t.color('black')
    t.fillcolor('grey')
    t.speed(0)
    t.up()
    t.left(90)
    t.forward(max(turtleHeightList)*40)
    t.write('The histogram shows the count of each character in the string "{}"'.format(forString), font=("Arial", 12, "normal"))
    t.right(180)
    t.forward(max(turtleHeightList)*40)
    t.left(90)
    t.down()
    t.begin_fill()


    for i in range(len(turtleHeightList)):
        t.left(90)
        t.forward(turtleHeightList[i] * 20)
        t.right(90)
        t.write('  key {} = {}'.format(keyList[i],turtleHeightList[i]), font=("Arial", 12, "normal"))
        t.forward(60)
        t.right(90)
        t.forward(turtleHeightList[i] * 20)
        t.left(90)

    t.end_fill()

    wn.exitonclick()

countAndDraw('banana')
