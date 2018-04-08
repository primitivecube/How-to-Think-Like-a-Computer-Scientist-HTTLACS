# Write a function that reverses its string argument.

def reverse(astring):
    reverseString = ""
    for ch in astring:
        reverseString = ch + reverseString
    return reverseString

print(reverse('hello'))
