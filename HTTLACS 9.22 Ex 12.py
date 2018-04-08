# Write a function that removes all occurrences of a string from another string.

def remove_all(subString, string):
    removeStart = None
    removeEnd = None
    newString = ''
    removeStartList = []
    removeEndList = []
    skipList = []

    for i in range (len(string)):
        if subString in string[i:i+len(subString)]:
            removeStart = i
            removeEnd = i+len(subString)
            removeStartList.append(removeStart)
            removeEndList.append(removeEnd)

        elif subString not in string:
            return string

    for a in range (len(removeStartList)):
        for i in range (removeStartList[a], removeEndList[a]):
            skipList.append(i)

    for i in range (len(string)):
        if i not in skipList:
            newString += string[i]

    return newString

print(remove_all('ana', 'banana'))


