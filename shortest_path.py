
# gets key with a minimum value of 'distance' that belong to 'unvisited'
def get_min_key(distance, unvisited):
    min_val = float('inf') 
    min_key = unvisited[0]
    for key, value in distance.items():
        if value <= min_val and key in unvisited:
            min_val = value
            min_key = key
    return min_key

def djikstra(G, origin, dest, attr):
    import networkx as nx
    unvisited = list(G.nodes())
    distance = {}
    parent = {}
    weight = nx.get_edge_attributes(G, attr)
    for node in G.nodes():
        distance[node] = float('inf') 
        parent[node] = None
    distance[origin] = 0

    while len(unvisited) != 0:
        current_node = get_min_key(distance, unvisited)
        unvisited.remove(current_node)
        for neighbor in G.neighbors(current_node):
            new_distance = distance[current_node] + weight[(current_node, neighbor)]
            if(distance[neighbor] > new_distance):
                distance[neighbor] = new_distance
                parent[neighbor] = current_node
    # Return path
    current = dest
    path = []
    while current:
        path.insert(0, current)
        current = parent[current]

    return path