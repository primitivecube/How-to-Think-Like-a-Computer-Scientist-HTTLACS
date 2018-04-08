def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price > 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        elif price < 0:
            print("ERROR - negative prices cannot be accepted")
        else:
            moreItems = False
    if total == 0 or count == 0:
        print("ERROR - data is required to compute average")
    else:
        average = total / count
        print('Total items:', count)
        print('Total $', total)
        print('Average price per item: $', average)

checkout()

