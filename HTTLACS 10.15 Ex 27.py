# Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:
# test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

# test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')
#
s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
# test(replace(s, 'om', 'am'),
#        'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')
#
# test(replace(s, 'o', 'a'),
#        'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')

def replace(s, old, new):
    return new.join(s.split(old))

print(replace(s,'om','am'))



