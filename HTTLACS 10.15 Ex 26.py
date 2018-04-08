# Although Python provides us with many list methods, it is good practice and very instructive
# to think about how they are implemented. Implement a Python function that works like the following:
#
# count
# in
# reverse
# index
# insert

aList = [1,2,3,4,5,5,'apple','banana','orange']

# count

def myCount(list,value):
    count = 0
    for item in list:
        if item == value:
            count += 1
    return count

print(myCount(aList,5))

# in

def myIn(list,value):
    for item in list:
        if item == value:
            return True
    return False

print(myIn(aList,10))

# reverse

def myReverse(list):
    cloneList = list[:] # clone the list
    reversedList = []
    for i in range (len(cloneList)):
        reversedList.append(cloneList.pop())
    return reversedList

print(myReverse(aList))

# index

def myIndex(list, value):
    index = -1
    for item in list:
        if item == value:
            index += 1
            return index
        else:
            index += 1
    return index

print(myIndex(aList,5))

# insert

def myInsert(list, value, index):
    breakList = list[0:index]
    breakList += [value]
    remainingList = list[index:]
    fixList = breakList + remainingList
    return fixList

print(myInsert(aList,'hat',5))





