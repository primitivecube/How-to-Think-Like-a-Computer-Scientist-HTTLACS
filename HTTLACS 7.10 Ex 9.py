def is_even(n):
    # your code here

    if n % 2 == 0:
        return True
    else:
        return False
def is_odd(n):
    return not is_even(n)

print(is_odd(-1))



