def fib2(n):
    if n <= 0:
        return 0

    a = list(range(100))
    if n == 1 or  n== 2:
        return 1

    a[0] = 0
    a[1] = 1
    for i in range(2,n+1):
       a[i] = a[i-1] + a[i-2]
    return a[n]
# check if the number of terms is valid
print(fib2(30))
