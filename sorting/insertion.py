def insertion_sort(a):
    i = 1
    while i < len(a):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j = j - 1
        i = i + 1


a = [53, 12, 15, 0, 4, 97, 22]
print(a)
insertion_sort(a)
print(a)
