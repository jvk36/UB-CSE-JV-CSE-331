# represents undirected graph with edge weights
class graph:
    def __init__(self, n, m, edges):
        self.n = n
        self.m = m
        # mark vertices as unexplored
        # adj_list holds a list of vertices, each vertex
        # is a list [vertex number, label, list of incident edges] where
        # List of incident edges is [vertex #1, vertex #2, edge weight, label]
        self.adj_list = [[i+1, 'UNEXPLORED', []] for i in range(n)]
        self.v_labels = ['UNEXPLORED' for _ in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            # add edge to the adjaceny list of corresponding vertex and mark as unexplored
            self.adj_list[u - 1][2].append([u, v, w, 'UNEXPLORED'])
            self.adj_list[v - 1][2].append([v, u, w, 'UNEXPLORED'])

    def vertex_nodes(self):
        return self.adj_list

    def vertices(self):
        return [i for i in range(1, self.n + 1)]

    def edges(self):
        ret = []
        for v in self.adj_list:
            for e in v[2]:
                ret.append(e)
        return ret

    # v is the vertex number
    def get_vertex_label(self, v):
        return self.adj_list[v-1][1]

    def set_vertex_label(self, v, label):
        self.adj_list[v-1][1] = label

    # e is the edge represented as (u, v, w)
    def get_edge_label(self, e):
        vertex = self.adj_list[e[0]-1]
        incident_edges = vertex[2]
        for edge in incident_edges:
            if edge[1] == e[1]:
                return edge[3]

    def set_edge_label(self, e, label):
        vertex = self.adj_list[e[0]-1]
        incident_edges = vertex[2]
        for edge in incident_edges:
            if edge[1] == e[1]:
                edge[3] = label

    def incident_edges(self, v):
        vertex = self.adj_list[v-1]
        return vertex[2]

    def opposite(self, e, u):
        if e[0] == u:
            return e[1]
        elif e[1] == u:
            return e[0]
        return -1
