myList = []
myList.append(76)
myList.append(92.3)
myList.append("hello")
myList.append(True)
myList.append(4)
myList.append(76)
print (myList)

myList2 = []
myList2 += [76]
myList2 += [92.3]
myList2 += ["hello"]
myList2 += [True]
myList2 += [4]
myList2 += [76]
print (myList2)

# Starting with the list of the previous exercise, write Python statements to do the following:

# a. Append "apple" and 76 to the list.
#. Insert the value "cat" at position 3.
#. Insert the value 99 at the start of the list.
#. Find the index of "hello".
#. Count the number of 76s in the list.
#. Remove the first occurrence of 76 from the list.
#. Remove True from the list using ``pop`` and ``index``.

myList.extend(['apple',76])
print (myList)
myList.insert(3,'cat')
print (myList)
myList.insert(0, 99)
print (myList)
print (myList.index('hello'))
print (myList.count(76))
myList.remove(76)
print (myList)
myList.pop(myList.index(True))
print (myList)

