import graph


n, m = [int(elem) for elem in input().split()]
l = []
for i in range(m):
    u, v, w = [int(elem) for elem in input().split()]
    l.append([u, v, w])

g = graph.graph(n, m, l)

v = 1
for v in g.vertex_nodes():
    print(f"Incident vertices and weights of vertex {v[0]}: ")
    print(f"{v[2]}")
