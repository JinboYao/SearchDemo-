def dfs(graph, start, goal):
    stack = [(start, [start])]  # 栈中的元素是(当前节点, 路径列表)
    while stack:
        (vertex, path) = stack.pop()  # 取出栈顶元素
        if vertex == goal:
            return path  # 如果当前节点是目标节点，则返回路径
        for next in graph[vertex]:  # 遍历当前节点的所有邻接节点
            if next not in path:  # 检查节点是否已在路径中，避免循环
                stack.append((next, path + [next]))  # 将节点和新路径加入栈
    return None  # 如果没有找到路径，则返回 None

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

# 使用提供的图进行搜索
path_dfs = dfs(graph, 'Arad', 'Bucharest')
print("DFS Path from Arad to Bucharest:", path_dfs)
