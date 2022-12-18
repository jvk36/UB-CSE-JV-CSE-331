import math


def max_profit(le, n, offset):
    if n < 2:
        return -1, offset, offset
    if n == 2:
        return le[1] - le[0], offset, offset+1
    n = math.floor(n / 2)
    n1, l1, r1 = max_profit(le[0:n], n, offset)
    n2, l2, r2 = max_profit(le[n:], len(le[n:]), offset+n)
    # print(f"n1 = {n1}, {l1}, {r1} n2 = {n2}, {l2}, {r2}")
    n3 = max(le[n:]) - min(le[0:n])
    l3 = offset + le[0:n].index(min(le[0:n]))
    r3 = offset + n + le[n:].index(max(le[n:]))
    retindex = [n1, n2, n3].index(max([n1, n2, n3]))
    retvalues = [(n1, l1, r1), (n2, l2, r2), (n3, l3, r3)]
    return retvalues[retindex]

in_count = int(input())
in_list = [int(input()) for _ in range(in_count)]
max_value, max_index1, max_index2 = max_profit(in_list, in_count, 0)

# print(in_list)
print(f"Maximum Profit = {max_value}, Buy Day: {max_index1+1}, Sell Day: {max_index2+1}")
