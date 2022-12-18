import math


def merge(b, c, n1, n2):
    a = []
    i = 0
    j = 0
    while i < n1 or j < n2:
        if j > (n2 - 1) or (i < n1 and b[i] <= c[j]):
            a.append(b[i])
            i = i + 1
        else:
            a.append(c[j])
            j = j + 1
    return a


def strong_count(b, c, n1, n2):
    count = 0
    i = 0
    j = 0
    while i < n1 or j < n2:
        if j > (n2 - 1) or (i < n1 and b[i] <= 2 * c[j]):
            i = i + 1
            count = count + j
        else:
            j = j + 1
    return count


def sort_and_count(a, n):
    if n == 1:
        return a, 0
    nf = math.floor(n/2)
    b, m1 = sort_and_count(a[:nf], nf)
    c, m2 = sort_and_count(a[nf:], n - nf)
    a = merge(b, c, nf, n - nf)
    m = strong_count(b, c, nf, n - nf)
    # print(f"m1 = {m1}, m2 = {m2}, m = {m}")
    return a, m + m1 + m2


in_count = int(input())
in_list = [int(input()) for _ in range(in_count)]
out_list, out_count = sort_and_count(in_list, in_count)
# print(out_list)
print(out_count)
