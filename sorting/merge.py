import math


def merge(b, c, n1, n2):
    a = []
    i = 0
    j = 0
    while i < n1 or j < n2:
        if j >= n2 or (i < n1 and b[i] <= c[j]):
            a.append(b[i])
            i = i + 1
        else:
            a.append(c[j])
            j = j + 1
    return a


def merge_sort(a, n):
    if n == 1:
        return a
    else:
        n = math.floor(n / 2)
        b = merge_sort(a[0:n], n)
        c = merge_sort(a[n:], len(a[n:]))
    return merge(b, c, len(b), len(c))


print(merge_sort([53, 12, 15, 0, 4, 97, 22], 7))