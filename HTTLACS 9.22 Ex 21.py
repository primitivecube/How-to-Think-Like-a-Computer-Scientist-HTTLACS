# Write a function called rot13 that uses the Caesar cipher to encrypt a message.
# The Caesar cipher works like a substitution cipher but each character is replaced by the character 13 characters
# to ‘its right’ in the alphabet. So for example the letter a becomes the letter n.
# If a letter is past the middle of the alphabet then the counting wraps around to the letter a
# again, so n becomes a, o becomes b and so on.
# Hint: Whenever you talk about things wrapping around its a good idea to think of modulo arithmetic.

def rot13(inputString):
    newString = ''
    alphaString = 'abcdefghijklmnopqrstuvwxyz'
    alphaUpper = alphaString.upper()
    for ch in inputString:
        if ch in alphaString:
            newIndex = (alphaString.index(ch) + 13) % 26
            newCh = alphaString[newIndex]
            newString += newCh
        elif ch in alphaUpper:
            newIndex = (alphaUpper.index(ch) + 13) % 26
            newCh = alphaUpper[newIndex]
            newString += newCh
        elif ch not in alphaString and ch not in alphaUpper:
            newString += ch
    return newString

print(rot13('Hello World!'))
print(rot13('Uryyb Jbeyq!'))


