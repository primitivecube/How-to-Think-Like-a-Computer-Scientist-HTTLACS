# Warning: running this program will overwrite any file in the same folder as this .py file that is named
# 'studentdata.txt'

#  The following sample file called studentdata.txt contains one line for each student in
# an imaginary class. The student’s name is the first thing on each line, followed by some exam scores. The number of scores might be different for each student.
# joe 10 15 20 30 40
# bill 23 16 19 22
# sue 8 22 17 14 32 17 24 21 2 9 11 17
# grace 12 28 21 45 26 10
# john 14 32 25 16 89
# Using the text file studentdata.txt write a program that prints out the names of students
# that have more than six quiz scores.

fileCreate = open('studentdata.txt', 'w')
list = [
'joe 10 15 20 30 40','bill 23 16 19 22',
'sue 8 22 17 14 32 17 24 21 2 9 11 17',
'grace 12 28 21 45 26 10',
'john 14 32 25 16 89']

for i in list:
    fileCreate.write(i + '\n')
fileCreate.close()

fileref = open('studentdata.txt', 'r')
for line in fileref:
    values = line.split()
    if len(values) > 7:
        print ('{} has more than six quiz scores'.format(values[0].capitalize()))
print()

fileref.close()

# Using the text file studentdata.txt (shown in exercise 1) write a program that calculates
# the average grade for each student,
# and print out the student’s name along with their average grade.

fileref = open('studentdata.txt', 'r')
for line in fileref:
    values = line.split()
    name = values.pop(0)
    sum = 0
    for i in values:
        sum += int(i)
    average = sum / len(values)
    print('{} has an average grade of {:.2f}'.format(name.capitalize(),average))
print()

fileref.close()

# Using the text file studentdata.txt (shown in exercise 1) write a program that calculates
# the minimum and maximum score for each student. Print out their name as well.

fileref = open('studentdata.txt', 'r')
for line in fileref:
    values = line.split()
    name = values.pop(0)
    valuesInt = []
    for i in values:
        valuesInt.append(int(i))
    valuesInt.sort()
    if len(valuesInt) > 1:
        min = valuesInt.pop(0)
        max = valuesInt.pop()
    else:
        print('{} only completed one quiz, with a score of {}'.format(name,valuesInt.pop()))
    print('{} has achieved a minimum score of {} and a maximum score of {}'.format(name.capitalize(),min,max))
print()

fileref.close()

