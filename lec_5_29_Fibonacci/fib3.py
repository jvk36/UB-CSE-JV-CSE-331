def fib3(n):
    if n <= 0:
        return 0

    if n == 1 or n== 2:
        return 1

    a = 1
    b = 1
    c = 1
    d = 0
    k = n-3
    while k != 0:
        # matrix multiplication ((a, b), (c, d)) * ((e, f), (g, h)) where latter is ((1, 1), (1, 0))
        # is ((ae+bg, af+bh), (ce+dg, cf+dh)) = ((a+b,a), (c+d, c))
        (a, b, c, d) = (a+b, a, c+d, c)
        k = k - 1
    # vector multiplication ((a, b), (c, d)) * ((e), (g))) where the latter is ((1),(1)) = (a+b, c+d)
    # Fibonacci of n is the first term a+b which is returned
    return a+b

# check if the number of terms is valid
print(fib3(30))
