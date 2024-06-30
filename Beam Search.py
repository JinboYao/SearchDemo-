from queue import PriorityQueue

def beam_search(graph, heuristics, start, goal, beam_width):
    # 创建优先队列，根据启发式值排序
    queue = PriorityQueue()
    # 入队初始节点（启发式值，路径）
    queue.put((heuristics[start], [start]))

    while not queue.empty():
        # 保存新扩展的路径
        new_paths = []
        # 在每一层展开 beam_width 个节点
        for _ in range(min(beam_width, queue.qsize())):
            _, path = queue.get()
            current_node = path[-1]

            # 检查是否到达目标节点
            if current_node == goal:
                return path

            # 遍历当前节点的邻接节点
            for neighbor in graph[current_node]:
                if neighbor not in path:  # 防止循环路径
                    new_path = path + [neighbor]
                    # 启发式评分用于优先队列排序
                    new_paths.append((heuristics[neighbor], new_path))

        # 仅保留启发式评分最低的 beam_width 个路径在队列中
        for new_path in sorted(new_paths, key=lambda x: x[0])[:beam_width]:
            queue.put(new_path)

    return "No path found"

# 使用你给出的图结构和启发式值
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

heuristics = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Fagaras': 176,
    'Pitesti': 98,
    'Bucharest': 0,
    'Giurgiu': 77,
    'Urziceni': 80,
    'Hirsova': 151,
    'Eforie': 161,
    'Vaslui': 199,
    'Iasi': 226,
    'Neamt': 234
}

start_city = 'Arad'
goal_city = 'Bucharest'
beam_width = 2  # Beam 宽度
path = beam_search(graph, heuristics, start_city, goal_city, beam_width)
print("Path found using Beam Search:", path)
