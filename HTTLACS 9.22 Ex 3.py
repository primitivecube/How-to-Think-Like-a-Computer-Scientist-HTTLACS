# Assign to a variable in your program a triple-quoted string that contains your favorite paragraph of text -
# perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.
# Write a function that counts the number of alphabetic characters (a through z, or A through Z)
# in your text and then keeps track of how many are the letter ‘e’.

import string

def count(para):
    alphaCount = 0
    eCount = 0
    for ch in para.lower():
        if ch in string.ascii_lowercase:
            alphaCount += 1
        if ch == 'e':
            eCount += 1
    if alphaCount == 1:
        ch_chs = 'character'
    else:
        ch_chs = 'characters'
    if eCount == 1:
        is_are = 'is'
    else:
        is_are = 'are'
    print("Your text contains {} alphabetic {}, of which {} ({:.1f}%) {} 'e'".format(alphaCount, ch_chs, eCount, (eCount / alphaCount * 100), is_are))

tenet = '''Know your Enemy'''

count(tenet)
