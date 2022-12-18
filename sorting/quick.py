import random


def partition(a, l, r):
    p = random.randint(l, r)
    a[p], a[l] = a[l], a[p]
    i = l
    j = r
    while True:
        while i < j and a[i] < a[j]:
            j = j - 1
        if i == j:
            break
        a[i], a[j] = a[j], a[i]
        i = i + 1
        while i < j and a[i] < a[j]:
            i = i + 1
        if i == j:
            break
        a[i], a[j] = a[j], a[i]
        j = j - 1
    return i


def quick_sort(a, l, r):
    if l >= r:
        return
    m = partition(a, l, r)
    quick_sort(a, l, m-1)
    quick_sort(a, m+1, r)

a = [53, 12, 15, 0, 4, 97, 22]
print(a)
quick_sort(a, 0, 6)
print(a)