# Give the Python interpreter’s response to each of the following from a continuous interpreter session:
#
# >>> d = {'apples': 15, 'bananas': 35, 'grapes': 12}
# >>> d['banana'] # invlaid syntax, no 'banana' in d (it should be 'bananas')
# >>> d['oranges'] = 20
# >>> len(d) # 4; having added oranges, there are now 4 items in d
# >>> 'grapes' in d # True
# >>> d['pears'] # KeyError, there is no key called 'pears'
# >>> d.get('pears', 0) # returns 0, because 0 is specified as the null return value
# >>> fruits = d.keys()
# >>> fruits.sort() # AtrributeError: 'dict_keys' object has no attribute 'sort'
# >>> print(fruits) # it prints all the keys in d, because fruits = d.keys()
# >>> del d['apples']
# >>> 'apples' in d # False, because the key 'apples' was deleted from d

# Be sure you understand why you get each result.
# Then apply what you have learned to fill in the body of the function below, and add code for the tests indicated:

def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity
    return inventory

# make these tests work...
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
#  test that 'strawberries' in new_inventory
print('strawberries' in new_inventory)
#  test that new_inventory['strawberries'] is 10
print(new_inventory['strawberries']==10)
add_fruit(new_inventory, 'strawberries', 25)
#  test that new_inventory['strawberries'] is now 35)
print(new_inventory['strawberries']==35)

