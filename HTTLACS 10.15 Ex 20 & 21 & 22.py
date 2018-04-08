# Write a function to count how many odd numbers are in a list.

def countOdd(list):
    oddCount = 0
    for number in list:
        if number % 2 ==1:
            oddCount += 1
    return oddCount

myList = [1,2,3,4,5,6,7,8,9]

print(countOdd(myList))

# Sum up all the even numbers in a list.

def sumEven(list):
    evenSum = 0
    for number in list:
        if number % 2 == 0:
            evenSum += number
    return evenSum

print(sumEven(myList))

# Sum up all the negative numbers in a list.

def sumNegatives(list):
    negSum = 0
    for number in list:
        if number < 0:
            negSum += number
    return  negSum

negList = [-1,-2,-3,-4,-5,-6,-7,-8,-9]
print(sumNegatives(negList))
