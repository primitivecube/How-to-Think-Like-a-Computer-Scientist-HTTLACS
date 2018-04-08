# Write a function called remove_dups that takes a string and creates a new string by only adding
# those characters that are not already present.
# In other words, there will never be a duplicate letter added to the new string.

def remove_dups(inputString):
    ch_list = []
    newString = ''
    for ch in inputString:
        if ch in ch_list:
            continue
        elif ch not in ch_list:
            newString += ch
            ch_list.append(ch)
    return newString

print(remove_dups("mississippi"))


