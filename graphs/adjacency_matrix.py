n, m = [int(elem) for elem in input().split()]
edges = []
for i in range(m):
    u, v, w = [int(elem) for elem in input().split()]
    edges.append((u, v, w))
adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    print(adj_matrix[i])
for i in range(n):
    for j in range(n):
        for k in edges:
            if k[0] in [i+1, j+1] and k[1] in [i+1, j+1]:
                adj_matrix[i][j] = k[2]
for i in range(n):
    print(adj_matrix[i])
