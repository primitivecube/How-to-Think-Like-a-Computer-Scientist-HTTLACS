# Count how many words in a list have length 5.

def countWords(list):
    count5 = 0
    for word in list:
        if len(word) == 5:
            count5 += 1
    return count5

listWords = ['apple', 'hello', 'world', 'it', 'is', 'sunny', 'today']

print(countWords(listWords))
