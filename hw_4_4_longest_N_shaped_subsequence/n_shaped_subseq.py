import math


def max_n_shaped_subseq(a):
    n = len(a) - 2
    opt = [[0 for _ in range(n + 2)] for _ in range(5)]
    # print(opt)
    opt[1][1] = - math.inf
    opt[2][1] = - math.inf
    opt[3][1] = - math.inf
    for i in range(2, n+1):
        for j in range(1, i):
            if j < i and a[j] < a[i]:
                opt[1][i] = max(opt[1][i], 1 + max(1, opt[1][j]))
            if j < i and a[j] > a[i]:
                opt[2][i] = max(opt[2][i], 1 + max(opt[1][j], opt[2][j]))
            if j < i and a[j] < a[i]:
                opt[3][i] = max(opt[3][i], 1 + max(opt[2][j], opt[3][j]))
    # print(opt)
    if max(opt[2]) <= 0 or max(opt[3]) <= 0:
        return -math.inf
    return max(max(opt[1]), max(opt[2]), max(opt[3]))


in_count = int(input())
in_list = [0 for _ in range(in_count+2)]
for i in range(1, in_count+1):
    in_list[i] = int(input())
print(in_list)
print(f"Length of longest N-shaped subsequence = {max_n_shaped_subseq(in_list)}")
