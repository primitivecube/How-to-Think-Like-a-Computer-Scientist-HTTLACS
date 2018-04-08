def isLeap(year):
    # your code here
    # True for leap years: which are multiples of four
    # (with the exception of years divisible by 100
    # but not by 400)
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

print(isLeap(2100))
