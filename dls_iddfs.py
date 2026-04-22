def dls(graph, node, goal, depth,path):
    if depth == 0 and node == goal:
        return path
    if depth > 0:
        for neighbor in graph[node]:
            res = dls(graph, neighbor, goal, depth-1, path+[neighbor])
            if res:
                return res
    return None

def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls(graph, start, goal, depth, [start])
        if result:
            return result
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("IDDFS path from A to F:", iddfs(graph, 'A', 'F', 3))