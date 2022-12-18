def max_indep_set(w):
    n = len(w[1]) - 2
    opt = [[0 for _ in range(n + 2)] for _ in range(5)]
    # print(opt)
    opt[1][1] = w[1][1]
    opt[2][1] = w[2][1]
    i = 2
    while i <= n:
        opt[1][i] = w[1][i] + max(opt[3][i-1], opt[2][i-1])
        opt[2][i] = w[2][i] + max(opt[3][i-1], opt[1][i-1])
        opt[3][i] = max(opt[3][i-1], opt[1][i-1], opt[2][i-1])
        i = i + 1
    # print(opt)
    return max(opt[1][n], opt[2][n], opt[3][n])

in_count = int(input())
in_list = [[0 for _ in range(in_count+2)] for _ in range(4)]
for i in range(1, 3):
    for j in range(1, in_count+1):
        in_list[i][j] = int(input())
# print(in_list)
print(f"Total weight of maximum weighted independent set = {max_indep_set(in_list)}")
