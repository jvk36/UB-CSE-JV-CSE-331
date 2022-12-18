def fib1(n):
    if n<= 0:
        return 0

    if n == 1 or n == 2:
       return 1
    else:
       return(fib1(n-1) + fib1(n-2))

# check if the number of terms is valid
print(fib1(30))
