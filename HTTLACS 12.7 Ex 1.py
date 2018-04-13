# Write a program that allows the user to enter a string.
# It then prints a table of the letters of the alphabet in alphabetical order which
# occur in the string together with the number of times each letter occurs. Case should be ignored.
# A sample run of the program might look this this:
# Please enter a sentence: ThiS is String with Upper and lower case Letters.
# a  2
# c  1
# d  1
# e  5
# g  1
# h  2
# i  4
# l  2
# n  2
# o  1
# p  2
# r  4
# s  5
# t  5
# u  1
# w  2
# $

# Working out the algorithm...
# forString = 'ThiS is String with upper and lower case Letters.'
#
# alphaDict = {}
# alphaString = 'abcdefghijklmnopqrstuvwxyz'
# for i in alphaString:
#     alphaDict[i] = 0
#
# print(alphaDict)
#
# for i in forString:
#     if i in alphaDict:
#         alphaDict[i] = forString.count(i)
#
# print(alphaDict)
#
# for i in alphaDict:
#     if alphaDict[i] > 0:
#         print('{}  {}'.format(i,alphaDict[i]))
# print('$')

# defining the function...

def getLetterCounts(forString):
    alphaDict = {}
    alphaString = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphaString:
        alphaDict[i] = 0

    for i in forString:
        if i in alphaDict:
            alphaDict[i] = forString.count(i)

    for i in alphaDict:
        if alphaDict[i] > 0:
            print('{}  {}'.format(i,alphaDict[i]))
    print('$')

getLetterCounts('ThiS is String with upper and lower case Letters.')

