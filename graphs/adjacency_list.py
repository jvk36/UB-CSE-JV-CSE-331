n, m = [int(elem) for elem in input().split()]
adj_list = [[] for _ in range(n)]
for i in range(m):
    u, v, w = [int(elem) for elem in input().split()]
    adj_list[u-1].append([v, w])
    adj_list[v-1].append([u, w])

v = 1
for edge_list in adj_list:
    if len(edge_list) > 0:
        print(f"Incident vertices and weights of vertex {v}: ")
    for e in edge_list:
        print(f"{e}")
    v = v + 1
