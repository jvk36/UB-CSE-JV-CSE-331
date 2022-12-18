def max_revenue(x, r):
    len_x = len(x) - 2
    opt = [0 for _ in range(len(x))]
    m_j = [0 for _ in range(len(x))]
    k = 1
    for i in range(2, len_x+1):
        for j in range(m_j[k]+1, i):
            if (x[i] - x[j]) > 5:
                m_j[i] = j
            else:
                break
        k = i
    opt[1] = r[1]
    for i in range(2, len_x+1):
        opt[i] = max(r[i] + opt[m_j[i]], opt[i-1])

    return max(opt)

in_count = int(input())
in_x = [0 for _ in range(in_count+2)]
in_r = [0 for _ in range(in_count+2)]
for i in range(1, in_count+1):
        in_x[i], in_r[i] = [int(a) for a in input().split()]
print(f"Maximum Revenue = {max_revenue(in_x, in_r)}")
