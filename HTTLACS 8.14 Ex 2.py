def print_triangular_numbers(n):
    # your code here
    tri_n = 0
    for i in range (1,n+1):
        tri_n += i
        print(i, "\t", tri_n)

print_triangular_numbers(5)
