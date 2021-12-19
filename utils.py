# Degree Connectivity
from networkx.algorithms.shortest_paths.generic import shortest_path


def degree_inflow(G, node):
    return G.in_degree(node)
def degree_outflow(G, node):
    return G.out_degree(node)
def degree(G, node):
    return G.degree(node)

def _path_length(path):
    return len(path) - 1

def closeness_centrality(G, node, weight):
    import shortest_path
    total_length = 0
    nodes = list(G.nodes())
    for dest in nodes:
        if dest != node:
            # path = shortest_path.dijkstra(G, source=node, target=dest, weight=weight)
            path = shortest_path.dijkstra(G, origin=node, dest=dest, attr=weight)
            total_length += _path_length(path)
    return total_length/len(nodes)

def get_path(G, src, dst, weight):
    try:
        import shortest_path
        return shortest_path.dijkstra(G, src, dst, weight)
    except:
        return []
    
def get_all_pathes(G, weight):
    pathes = {}
    for src in G.nodes():
        for dst in G.nodes():
            if src != dst:
                path = get_path(G, src, dst, weight)
                if len(path) > 1:
                    pathes[src + '_' + dst] = path
    return pathes

def between_centrality(G, node, pathes):
    count = 0
    for path in pathes.values():
        if node in path:
            count += 1
    return count

# Network Density
def network_density(G):
    nodes = G.nodes()
    total_degree = 0
    for node in nodes:
        total_degree += degree(G, node)
    return total_degree/(len(nodes) * (len(nodes) - 1))

# Network Diameter
def network_diameter(G, weight):
    pathes = get_all_pathes(G, weight)
    path_len = 0
    for path in pathes.values():
        if len(path) > path_len:
            path_len = len(path)
    return path_len

# Network Average Path Length
def network_average_path_length(G, weight):
    pathes = get_all_pathes(G, weight)
    total_path_len = 0
    for path in pathes.values():
        total_path_len += len(path)
    return total_path_len/len(pathes)