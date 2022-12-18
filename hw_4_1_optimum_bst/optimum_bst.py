import math


def opt_bst(f):
    n = len(f)
    opt = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    # print(opt)
    for i in range(1, n+1):
        opt[i][i] = f[i-1]
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            term = [0 for _ in range(j + 1)]
            fsum = 0
            for k in range(j-i, j + 1):
                term[k] = opt[j-i][k - 1] + opt[k + 1][j]
                fsum = fsum + f[k-1]
            # print(f"term = {term}, fsum = {fsum}")
            opt[j-i][j] = min(term[(j-i):]) + fsum
            # print(f"opt j-i, j, value = {j-i}, {j}, {opt[j-i][j]}")
    # print(opt)
    return opt[1][n]

in_count = int(input())
in_list = [int(input()) for _ in range(in_count)]
# print(in_list)
print(f"Cost of Optimum BST = {opt_bst(in_list)}")
