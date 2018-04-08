# Write a function that will return the number of digits in an integer.

def getNumDigits(integer):
    string = str(integer)
    return len(string)

print(getNumDigits(999))
