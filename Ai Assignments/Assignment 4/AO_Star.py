def Cost(H, path, weight=1):
    cost = {}
    if 'AND' in path:
        AND_nodes = path['AND']
        Path_A = ' AND '.join(AND_nodes)
        PathA = sum(H[node] + weight for node in AND_nodes)
        cost[Path_A] = PathA

    if 'OR' in path:
        OR_nodes = path['OR']
        Path_B = ' OR '.join(OR_nodes)
        PathB = min(H[node] + weight for node in OR_nodes)
        cost[Path_B] = PathB
    return cost


def update_cost(H, paths, weight=1):
    Main_nodes = list(paths.keys())
    Main_nodes.reverse()
    least_cost = {}
    for key in Main_nodes:
        path = paths[key]
        print(key, ':', paths[key], '>>>', Cost(H, path, weight))
        c = Cost(H, path, weight)
        H[key] = min(c.values())
        least_cost[key] = Cost(H, path, weight)
    return least_cost


def shortest_path(Start, Updated_cost, G):
    Path = Start
    if Start in Updated_cost.keys():
        Min_cost = min(Updated_cost[Start].values())
        key = list(Updated_cost[Start].keys())
        values = list(Updated_cost[Start].values())
        Index = values.index(Min_cost)

        Next = key[Index].split()
        if len(Next) == 1:

            Start = Next[0]
            Path += '<--' + shortest_path(Start, Updated_cost, G)

        else:
            Path += '<--(' + key[Index] + ') '

            Start = Next[0]
            Path += '[' + shortest_path(Start, Updated_cost, G) + ' + '

            Start = Next[-1]
            Path += shortest_path(Start, Updated_cost, G) + ']'

    return Path


G = {'A': -1, 'B': 5, 'C': 2, 'D': 4, 'E': 7, 'F': 9, 'G': 3, 'H': 0, 'I': 0, 'J': 0}

paths = {
    'A': {'OR': ['B'], 'AND': ['C', 'D']},
    'B': {'OR': ['E', 'F']},
    'C': {'OR': ['G'], 'AND': ['H', 'I']},
    'D': {'OR': ['J']}
}
weight = 1
print('Updated Cost :')
Updated_cost = update_cost(G, paths, weight=1)
print('Shortest Path :\n', shortest_path('A', Updated_cost, G))
