from queue import PriorityQueue

def best_first_search(graph, heuristics, start, goal):
    # 创建一个优先队列
    visited = set()
    queue = PriorityQueue()
    queue.put((heuristics[start], [start]))

    while not queue.empty():
        # 获取启发式值最小的节点
        (cost, path) = queue.get()
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)

        # 如果达到目标节点
        if node == goal:
            return path

        # 探索相邻节点
        for adjacent in graph[node]:
            if adjacent not in visited:
                new_path = list(path)
                new_path.append(adjacent)
                queue.put((heuristics[adjacent], new_path))

    return "No path found"

# 图的邻接列表表示，确保每个节点都定义了
graph = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Craiova', 'Sibiu', 'Pitesti'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Craiova', 'Rimnicu Vilcea', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}


# 启发式值，从你的图中提取
heuristics = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

# 从 Arad 到 Bucharest 的最佳路径
path = best_first_search(graph, heuristics, 'Arad', 'Bucharest')
print("Path found:", path)