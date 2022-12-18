import graph


def bfsv(g, s):
    l = [[s]]
    g.set_vertex_label(s, 'VISITED')
    i = 0
    while l[i]:
        l.append([])
        for v in l[i]:
            for e in g.incident_edges(v):
                if g.get_edge_label(e) == 'UNEXPLORED':
                    w = g.opposite(e, v)
                    if g.get_vertex_label(w) == 'UNEXPLORED':
                        g.set_edge_label(e, 'DISCOVERY')
                        g.set_vertex_label(w, 'VISITED')
                        l[i+1].append(w)
                    else:
                        g.set_edge_label(e, 'CROSS')
        l[i].clear()
        i = i + 1


def bfs(g):
    for u in g.vertices():
        g.set_vertex_label(u, 'UNEXPLORED')
    for e in g.edges():
        g.set_edge_label(e, 'UNEXPLORED')
    for v in g.vertices():
        if g.get_vertex_label(v) == 'UNEXPLORED':
            bfsv(g, v)


n, m = [int(elem) for elem in input().split()]
l = []
for i in range(m):
    u, v, w = [int(elem) for elem in input().split()]
    l.append([u, v, w])

g = graph.graph(n, m, l)
bfs(g)

print("Discovery edges from BFS: ")
i = 1
for e in g.edges():
    if g.get_edge_label(e) == 'DISCOVERY':
        print(f"Edge {i}: {e}")
        i = i + 1
