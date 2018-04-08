def is_prime(n):
    # your code here
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print(is_prime(22))


import random
print(random.randint(-1,5))
