# Write a function that mirrors its string argument,
# generating a string containing the original string and the string backwards.

def mirror(astring):
    reverseString = ""
    for ch in astring:
        reverseString = ch + reverseString
    return astring+reverseString

print(mirror('hello'))
