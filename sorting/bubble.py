def bubble_sort(a):
    n = len(a)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


a = [53, 12, 15, 0, 4, 97, 22]
bubble_sort(a)
print(a)
