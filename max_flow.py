# G - graph, s - source, t - sink, weight - attribute
def edmonds_karp(G, s, t, weight):
    # Init capacities
    flow_edges = {}
    flow_edges_res = {}
    for i, j in G.edges():
        flow_edges[str(i) + '_' + str(j)] = [0, G.edges[i,j][weight]]
        flow_edges_res[str(j) + '_' + str(i)] = [0, 0]
    flow = 0

    while (True):
        parent = [-1] * len(flow_edges)
        q = []
        q.append(s)
        while (len(q) != 0):
            i = q[0]
            q.pop(0)
            for j in list(G.neighbors(i)):
                tmp_edge = flow_edges[str(i) + '_' + str(j)]
                if (parent[j] == -1 and (j != s) and tmp_edge[1] > tmp_edge[0]):
                    parent[j] = i
                    q.append(j)
            if parent[t] != -1:
                # we found aug path
                df = float('inf')
                t_local = t
                i = parent[t_local]
                while (i != -1):
                    tmp_edge = flow_edges[str(i) + '_' + str(t_local)]
                    df = min(df, tmp_edge[1] - tmp_edge[0])
                    t_local = i
                    i = parent[t_local]
                #update flows
                t_local = t
                i = parent[t_local]
                while (i != -1):
                    tmp_edge = flow_edges[str(i) + '_' + str(t_local)]
                    tmp_edge_res = flow_edges_res[str(t_local) + '_' + str(i)]
                    tmp_edge[0] += df
                    tmp_edge_res[0] -= df
                    t_local = i
                    i = parent[t_local]
                flow += df
        if (parent[t] == -1):
            break
    return flow