# Modify this code so it prints each subtotal, the total cost, and average price to exactly two decimal places.

# def checkout():
#     total = 0
#     count = 0
#     moreItems = True
#     while moreItems:
#         price = float(input('Enter price of item (0 when done): '))
#         if price != 0:
#             count = count + 1
#             total = total + price
#             print('Subtotal: $', total)
#         else:
#             moreItems = False
#     average = total / count
#     print('Total items:', count)
#     print('Total $', total)
#     print('Average price per item: $', average)
#
# checkout()

def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: ${:.2f}'.format(total))
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total ${:.2f}'.format(total))
    print('Average price per item: ${:.2f}'.format(average))

checkout()
