# Write a function that removes the first occurrence of a string from another string.

def remove(subString, string):
    removeStart = None
    removeEnd = None
    for i in range (len(string)):
        if subString in string[i:i+len(subString)]:
            removeStart = i
            removeEnd = i+len(subString)
            break
        elif subString not in string:
            return string

    newString = string[:removeStart]+string[removeEnd:]

    return newString

print(remove('an', 'banana'))
