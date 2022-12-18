import math


def peak(l, n, ret):
    if n == 1 or (n == 2 and l[0] > l[1]):
        return ret + 1
    if n == 2 and l[0] < l[1]:
        return ret + 2
    n = math.floor(n/2)
    if l[n-1] < l[n] > l[n+1]:
        return ret + n + 1
    if l[n-1] < l[n] < l[n+1]:
        ret = ret + n
        return peak(l[n:], len(l[n:]), ret)
    if l[n-1] > l[n] > l[n+1]:
        return peak(l[0:n], n, ret)
    return -1

in_count = int(input())
in_list = [int(input()) for _ in range(in_count)]
print(peak(in_list, in_count, 0))
# print(in_list)

