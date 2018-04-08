# Write a function that removes all occurrences of a given letter from a string.

# def remove_letter(theLetter, theString):
#     return theString.replace(theLetter,'')

# print(remove_letter('p','apple'))

# and without using .replace...

def remove_letter(theLetter, theString):
    newString = ''
    for ch in theString:
        if ch != theLetter:
            newString += ch
    return newString

print(remove_letter('p','apple'))
