import heapq

def a_star(graph, start, goal, heuristic):
    pq = [(0, start, [start])]
    g_cost = {start: 0}

    while pq:
        f, node, path = heapq.heappop(pq)

        if node == goal:
            return path
        
        for neighbor, cost in graph[node]:
            new_g = g_cost[node] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic[neighbor]
                heapq.heappush(pq, (f_cost, neighbor, path + [neighbor]))
    return None

graph_cost = {
    'A' : [('B', 1), ('C', 3)],
    'B' : [('D', 1), ('E', 4)],
    'C' : [('F', 2)],
    'D' : [],
    'E' : [('F', 1)],
    'F' : []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 3,
    'F': 0
}

print("A* path from A to F:", a_star(graph_cost, 'A', 'F', heuristic))