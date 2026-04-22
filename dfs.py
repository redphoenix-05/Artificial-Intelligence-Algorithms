def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    
    path.append(start)
    
    if start == goal:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in path:
            result = dfs(graph, neighbor, goal, path.copy())
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

print("DFS path from A to F:", dfs(graph, 'A', 'F'))