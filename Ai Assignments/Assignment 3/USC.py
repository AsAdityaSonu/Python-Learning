import math


def USC(start, end_node):
    queue = [(0, start)]  # (dis, starting node)
    dist = {node: math.inf for node in graph}
    dist[start] = 0
    # print(start)
    while queue:
        print(queue)

        queue.sort()
        distance, curr = queue.pop(0)
        if curr == end_node:
            return dist[end_node]
        if dist[curr] < distance:
            print("dist[curr] ", dist[curr])
            continue
        for i, weight in graph[curr].items():
            print('i, weight ', i, weight)
            new_distance = distance + weight
            if new_distance < dist[i]:
                dist[i] = new_distance
                queue.append((new_distance, i))
        print()
    return math.inf


graph = {
    'S': {'A': 1, 'B': 5, 'C': 15},
    'A': {'S': 1, 'B': 4, 'G': 10},
    'B': {'S': 5, 'A': 4, 'G': 5},
    'C': {'S': 15, 'G': 5},
    'G': {'A': 10, 'B': 5, 'C': 5}
}

print("Cost from S to G:", USC('S', 'G'))
