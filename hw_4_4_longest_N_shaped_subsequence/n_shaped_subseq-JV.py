import math


# returns opt[i] containing the largest increasing subsequence
# ending at i
def lis_e(a):
    opt = [0 for _ in range(len(a))]
    len_a = len(a) - 2
    for i in range(1, len_a+1):
        opt[i] = 1
    for i in range(1, len_a+1):
        for j in range(1, i):
            if a[j] < a[i]:
                opt[i] = max(opt[i], 1 + opt[j])
    return opt


# returns opt[i] containing the largest decreasing subsequence
# ending at i
def lds_e(a):
    opt = [0 for _ in range(len(a))]
    len_a = len(a) - 2
    for i in range(1, len_a+1):
        opt[i] = 1
    for i in range(1, len_a+1):
        for j in range(1, i):
            if a[j] > a[i]:
                opt[i] = max(opt[i], 1 + opt[j])
    return opt


# returns opt[i] containing the largest increasing subsequence
# starting at i
def lis_s(a):
    opt = [0 for _ in range(len(a))]
    len_a = len(a) - 2
    for i in range(1, len_a+1):
        opt[i] = 1
    for i in range(len_a, 0, -1):
        for j in range(i-1, 0, -1):
            if a[j] < a[i]:
                opt[j] = max(opt[j], 1 + opt[i])
    return opt


# returns opt[i] containing the largest decreasing subsequence
# starting at i
def lds_s(a):
    opt = [0 for _ in range(len(a))]
    len_a = len(a) - 2
    for i in range(1, len_a+1):
        opt[i] = 1
    for i in range(len_a, 0, -1):
        for j in range(i-1, 0, -1):
            if a[j] > a[i]:
                opt[j] = max(opt[j], 1 + opt[i])
    return opt


def n_shaped_subseq(a):
    # print(f"lis = {lis(a)}")
    # print(f"lds = {lds(a)}")
    # print(f"lis_2d = {lis_2d(a)}")
    # print(f"lds_2d = {lds_2d(a)}")
    len_a = len(a) - 2
    s1 = lis_s(a)
    s2 = lis_e(a)
    d1 = lds_s(a)
    d2 = lds_e(a)
    max_value = 0
    for i in range(2, len_a+1):
        for j in range(i+1, len_a+1):
            cur_value = s2[i] + d2[j] - d1[i] + max(s2[j+1:]) - s1[j] - 2
            if max_value < cur_value:
                max_value = cur_value
    return max_value


in_count = int(input())
in_a = [0 for _ in range(in_count+2)]
for i in range(1, in_count+1):
        in_a[i] = int(input())
#print(in_a)
print(f"Length of the longest N shaped subsequence = {n_shaped_subseq(in_a)}")
