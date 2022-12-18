def get_lightest_edge(gamma, adj_list):
    min_w = 1000001
    min_u = 1
    min_x = 1
    for x in gamma:
        for nbr in adj_list[x-1]:
            u = nbr[0]
            if u not in gamma and nbr[1] < min_w:
                min_w = nbr[1]
                min_u = u
                min_x = x
    return min_u, min_x, min_w


n, m = [int(elem) for elem in input().split()]
adj_list = [[] for _ in range(n)]
for i in range(m):
    u, v, w = [int(elem) for elem in input().split()]
    adj_list[u-1].append([v, w])
    adj_list[v-1].append([u, w])
gamma = [1]
mst = []
total_weight = 0
while len(gamma) != n:
    (u, x, w) = get_lightest_edge(gamma, adj_list)
    total_weight = total_weight + w
    gamma.append(u)
    mst.append((x, u))

print(total_weight)
# for u, v in mst:
#     print(f"{u} {v}")
