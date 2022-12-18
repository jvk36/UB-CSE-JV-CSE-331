def fib2a(n):
    if n <= 0:
        return 0

    if n == 1 or n== 2:
        return 1

    a = 0
    b = 1
    for i in range(2,n+1):
       c = a + b
       a = b
       b = c

    return c
# check if the number of terms is valid
print(fib2a(30))
