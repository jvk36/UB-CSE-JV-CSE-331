import heapq


def get_lightest_edge(gamma, adj_list):
    min_w = 1000001
    min_u = 1
    min_x = 1
    for x in gamma:
        for i in range(len(adj_list[x-1])):
            nbr = heapq.heappop(adj_list[x-1])
            u = nbr[1]
            if u not in gamma:
                heapq.heappush(adj_list[x-1], nbr)
                if nbr[0] < min_w:
                    min_w = nbr[0]
                    min_u = u
                    min_x = x
                break
    return min_u, min_x, min_w


n, m = [int(elem) for elem in input().split()]
adj_list = [[] for _ in range(n)]
for i in range(m):
    u, v, w = [int(elem) for elem in input().split()]
    heapq.heappush(adj_list[u-1], (w, v))
    heapq.heappush(adj_list[v-1], (w, u))
gamma = [1]
mst = []
total_weight = 0
while len(gamma) != n:
    (u, x, w) = get_lightest_edge(gamma, adj_list)
    total_weight = total_weight + w
    gamma.append(u)
    mst.append((x, u))

print(total_weight)
for u, v in mst:
    print(f"{u} {v}")
