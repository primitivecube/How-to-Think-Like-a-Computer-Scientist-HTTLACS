# Print out a neatly formatted multiplication table, up to 12 x 12.

def xTable (number):
    """Prints a neat multiplication table up to 32 x 32; anything producing more than one 4-digit result in a row will cause the table to skew"""
    list = ['x']
    index = 0

    for multiplicand in range (1,number+1): # generate multiplicand list
        list.append(multiplicand)

    for xMultiplicand in list: # generate top row of multiplication table
        print(xMultiplicand, end = "\t\t")
    print()

    for yMultiplicand in range (1,number+1): # generate left column of multiplication table
        index += 1
        print(list[index], end = "\t\t")
        for factor in range (1,number+1): # generate products of all factors in multiplication table
            print((list[index]*factor), end = "\t\t")
        print()

xTable(12)
