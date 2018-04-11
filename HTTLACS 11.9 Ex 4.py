# Warning: Running this program will overwrite any files in the same folder as this .py file that are
# named 'labdata.txt'

# I was not familiar with regression nor sigma notation when I started writing this program.
# The following websites were essential in understanding this question:

# http://www.dummies.com/education/math/calculus/how-to-use-sigma-notation/
# http://www.dummies.com/education/math/statistics/how-to-calculate-a-regression-line/
# http://www.dummies.com/education/math/statistics/finding-standard-deviation-in-a-statistical-sample/
# http://www.dummies.com/education/math/statistics/how-to-calculate-a-correlation/
# http://www.dummies.com/education/math/statistics/using-linear-regression-to-predict-an-outcome/
# http://www.dummies.com/education/math/statistics/how-to-interpret-a-correlation-coefficient-r/

# Here is a file called labdata.txt that contains some sample data from a lab experiment.

# 44 71
# 79 37
# 78 24
# 41 76
# 19 12
# 19 32
# 28 36
# 22 58
# 89 92
# 91 6
# 53 7
# 27 80
# 14 34
# 8 81
# 80 19
# 46 72
# 83 96
# 88 18
# 96 48
# 77 67

# Interpret the data file labdata.txt such that each line contains a an x,y coordinate pair.
# Write a function called plotRegression that reads the data from this file and
# uses a turtle to plot those points and a best fit line according to the following formulas:
# (HTTLACS shows the formula for linear regression)

# To meet the objective of the quiz, we need to use functions that read a file called labdata.txt
# I will write the program so that it creates the labdata.txt file (as a string), then interprets it to produce the
# following lists (of integers):
# listX = [44,79,78,41,19,19,28,22,89,91,53,27,14,8,80,46,83,88,96,77]
# listY = [71,37,24,76,12,32,36,58,92,6,7,80,34,81,19,72,96,18,48,67]

fileCreate = open('labdata.txt', 'w')
fileListX = [44,79,78,41,19,19,28,22,89,91,53,27,14,8,80,46,83,88,96,77]
fileListY = [71,37,24,76,12,32,36,58,92,6,7,80,34,81,19,72,96,18,48,67]

for i in range(len(fileListX)):
    fileCreate.write(str(fileListX[i])+' '+str(fileListY[i])+'\n')
fileCreate.close()

listX = []
listY = []

fileRef = open('labdata.txt', 'r')
for line in fileRef:
    print(line)
    values = line.split()
    listX.append(int(values[0]))
    listY.append(int(values[1]))
print(listX)
print(listY)

fileRef.close()

print(len(listX),'lenlistX')

sumX = 0

for i in listX:
    sumX += i
print(sumX, 'sumX')
print(type(listX[0]))

meanX = sumX / len(listX) # mean of x is the first of five key variables in the linear regression formula

print(meanX, 'meanX')

print(len(listY),'lenlistY')
sumY = 0
for i in listY:
    sumY += i
print(sumY, 'sumY')
print(type(listY[0]))

meanY = sumY / len(listY) # mean of y is the second of five key variables in the linear regression formula

print(meanY, 'meanY')

stdDevXSum = 0

for i in range(len(listX)):
    nominator = (i - meanX) ** 2
    denominator = len(listX) - 1
    stdDevXSum += nominator / denominator
print(stdDevXSum, 'stdDevXSum')

stdDevX = (stdDevXSum) ** 0.5 # standard deviation of x is the third of five key variables in the linear regression formula

print(stdDevX, 'stdDevX')
print(stdDevX * stdDevX, 'square of stdDevX')

stdDevYSum = 0

for i in range(len(listY)):
    nominator = (i - meanY) ** 2
    denominator = len(listY) - 1
    stdDevYSum += nominator / denominator
print(stdDevYSum, 'stdDevYSum')

stdDevY = (stdDevYSum) ** 0.5 # standard deviation of y is the fourth of five key variables in the linear regression formula

print(stdDevY, 'stdDevY')
print(stdDevY * stdDevY, 'square of stdDevY')

rXY = 0 # a sum necessary for calculating 'r'

for i in range(len(listX)):
    x = listX[i] - meanX
    y = listY[i] - meanY
    xy = x * y
    rXY += xy

print(rXY, 'rXY')

divXY = rXY / (stdDevX * stdDevY) # division necessary for calculating 'r'

r = divXY / (len(listX) - 1) # r is the fifth of five key variables in the linear regression formula
                             # r is the correlation coefficient. It measures the strength of the relationship
                             # between two variables, and is always between +1 and -1.
                             # Values close to +1/-1 have a strong relationship, those close to 0 have no relationship.

print(r,'r')

# the r value is very close to zero, therefore there is no relationship between the variables,
# and therefore the data is not suitable for a linear regression. However, to complete the exercise,
# we'll plot a linear regression line anyway.

m = r * (stdDevY / stdDevX) # m is the slope
print(m, 'm')

b = meanY - (m * meanX) # b is the y-intercept
print(b, 'b')

provideX = max(listX)   # This used as the last x coordinate to complete the linear regression line.
                        # Any value of x from the data can be plugged into the folowing formula to find y
                        # at that point, and thus plot the linear regression line to that point.

print(provideX, 'provideX')

findY = meanY + (m * (provideX - meanX)) # Formula to find y, given an x value.
                                         # This is used as the last y coordinate to complete the linear regression line.

print(findY, 'findY')

import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(0,0,100,100)
for i in range(len(listX)):
    t.up()
    t.goto(listX[i], listY[i])
    t.dot()
t.up()
t.goto(0,b) # go to the y-intercept
t.color('green')
t.dot()
t.down()
t.begin_fill()
t.goto(provideX, findY) # complete the linear regression line across the scatter plot
wn.exitonclick()

# As you can see, the linear regression line is a nearly arbitrary line across the centre of the scatterplot.
# Given the lack of relationship (r) between the variables, this is what we expected to see.
