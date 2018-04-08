# Sum all the elements in a list up to but not including the first even number.

import random

def sumUntilEven(list):
    sum = 0
    for number in list:
        if number % 2 == 0:
            break
        else:
            sum += number
            print (sum)
    return sum

listNums = []
for i in range (20):
    listNums.append(random.randint(0,100))

print(sumUntilEven(listNums))

# Count how many words occur in a list up to and including the first occurrence of the word “sam”.

def count(list):
    wordCount = 0
    for word in list:
        if word == 'sam' or word == 'Sam' or word == 'SAM':
            break
        else:
            wordCount += 1
    return  wordCount

listWords = ['My', 'name', 'is', 'Sam']

print(count(listWords))
