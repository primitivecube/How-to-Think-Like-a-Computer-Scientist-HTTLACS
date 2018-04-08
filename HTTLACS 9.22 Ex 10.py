# Write a function that counts how many non-overlapping occurrences of a substring appear in a string.

# Note: HTTLACS test data accepts the code below as a PASS for all test. However, in my opinion, it doesn't meet the
# definition of 'non-overlapping' (which isn't explained on the website). In my opinion, non-overlapping means that
# occurrences should not share any index values. Here is the code that passes the test, but actually does share index
# values:

def count(subString, string):
    counter = 0
    sliceFound = ''
    for i in range (len(string)):
        if subString in string[i:i+len(subString)]:
            counter += 1
            sliceFound += '{}:{} \n'.format(i, i+len(subString))

    if counter == 1:
        time_s = 'time'
    else:
        time_s = 'times'

    return "{} was found {} {} at the following slices:\n{}".format(subString, counter, time_s, sliceFound)

print(count('ana', 'bananananananana'))

# And here is the version that doesn't pass the test, but actually meets the logical interpretation of 'non-overlapping'
# where no index values are shared between occurrences:

def count(subString, string):
    step = 0
    counter = 0
    sliceFound = ''
    for i in range (len(string)):
        if subString in string[i+step:i+len(subString)+step]:
            counter += 1
            sliceFound += '{}:{} \n'.format(i+step, i+len(subString)+step)
            step += len(subString)-1

    if counter == 1:
        time_s = 'time'
    else:
        time_s = 'times'

    return "{} was found {} {} at the following non-overlapping slices:\n{}".format(subString, counter, time_s, sliceFound)

print(count('ana', 'bananananananana'))
