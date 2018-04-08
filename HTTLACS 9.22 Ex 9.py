# Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!).

def is_palindrome(astring):
    reverseString = ""
    for ch in astring:
        reverseString = ch + reverseString
    if astring == reverseString:
        return True
    else:
        return False

print(is_palindrome('level'))
