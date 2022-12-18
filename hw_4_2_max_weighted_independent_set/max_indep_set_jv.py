import math


def max_indep_set(w):
    len_w = len(w[1]) - 2
    opt = [[0 for _ in range(len_w + 2)] for _ in range(4)]
    opt1 = [[0 for _ in range(len_w + 2)] for _ in range(4)]
    # print(opt)
    opt[1][1] = w[1][1]
    n = 2
    while True:
        opt[2][n] = max(w[2][n] + opt[1][n-1], opt[1][n])
        if n == len_w:
            return opt[2][n]
        opt1[2][n] = max(w[2][n] + opt[1][n-1], opt[2][n-1])
        n = n + 1
        opt[1][n] = max(w[1][n] + opt1[2][n-1], opt[2][n-1])

    return -1

in_count = int(input())
in_list = [[0 for _ in range(in_count+2)] for _ in range(4)]
for i in range(1, 3):
    for j in range(1, in_count+1):
        in_list[i][j] = int(input())
# print(in_list)
print(f"Total weight of maximum weighted independent set = {max_indep_set(in_list)}")
