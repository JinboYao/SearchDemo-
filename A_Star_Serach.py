# A* 算法的关键组件：
# g(n)：从起点到任意顶点 n 的实际成本路径。
# h(n)：从顶点 n 到目标的估计成本（启发式），这是一个估计值，用于评估剩余距离的成本。
# f(n) = g(n) + h(n)：f(n) 是每个节点的评分，它是 g(n) 和 h(n) 的和，用于决定节点的遍历顺序。
# 算法步骤：
# 初始化开放列表（open list）和闭合列表（closed list）。
# 将起始节点放入开放列表中。
# 当开放列表不为空时，执行以下操作：
# 从开放列表中取出 f 值最小的节点作为当前节点（current node）。
# 检查当前节点是否为目标节点。如果是，那么算法结束，路径被找到。
# 对于当前节点的每个邻接节点，如果它不在闭合列表中，计算它的 g(n)，h(n)，和 f(n) 值，并将其添加到开放列表中。
# 如果邻接节点已经在开放列表中，检查通过当前节点到达它的路径是否更好（即检查 g 值是否更小）。如果是，则更新其 f，g 和 h 值以及父节点。
# 将当前节点移至闭合列表。
from queue import PriorityQueue

def a_star_search(graph, costs, heuristics, start, goal):
    # 创建优先队列
    open_list = PriorityQueue()
    open_list.put((heuristics[start], start))
    came_from = {}
    cost_so_far = {start: 0}

    while not open_list.empty():
        current = open_list.get()[1]

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor in graph[current]:
            new_cost = cost_so_far[current] + costs[(current, neighbor)]
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristics[neighbor]
                open_list.put((priority, neighbor))
                came_from[neighbor] = current

    return "No path found"

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from.get(current, start)
    path.append(start)
    path.reverse()
    return path

# 定义图的结构
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
    'Bucharest': ['Fagaras', 'Pitesti'],
}

# 定义边的成本
costs = {
    ('Arad', 'Zerind'): 75,
    ('Arad', 'Sibiu'): 140,
    ('Arad', 'Timisoara'): 118,
    ('Zerind', 'Arad'): 75,
    ('Zerind', 'Oradea'): 71,
    ('Oradea', 'Zerind'): 71,
    ('Oradea', 'Sibiu'): 151,
    ('Timisoara', 'Arad'): 118,
    ('Timisoara', 'Lugoj'): 111,
    ('Lugoj', 'Timisoara'): 111,
    ('Lugoj', 'Mehadia'): 70,
    ('Mehadia', 'Lugoj'): 70,
    ('Mehadia', 'Drobeta'): 75,
    ('Drobeta', 'Mehadia'): 75,
    ('Drobeta', 'Craiova'): 120,
    ('Craiova', 'Drobeta'): 120,
    ('Craiova', 'Rimnicu Vilcea'): 146,
    ('Craiova', 'Pitesti'): 138,
    ('Rimnicu Vilcea', 'Craiova'): 146,
    ('Rimnicu Vilcea', 'Sibiu'): 80,
    ('Rimnicu Vilcea', 'Pitesti'): 97,
    ('Sibiu', 'Arad'): 140,
    ('Sibiu', 'Oradea'): 151,
    ('Sibiu', 'Fagaras'): 99,
    ('Sibiu', 'Rimnicu Vilcea'): 80,
    ('Fagaras', 'Sibiu'): 99,
    ('Fagaras', 'Bucharest'): 211,
    ('Pitesti', 'Craiova'): 138,
    ('Pitesti', 'Rimnicu Vilcea'): 97,
    ('Pitesti', 'Bucharest'): 101,
    ('Bucharest', 'Fagaras'): 211,
    ('Bucharest', 'Pitesti'): 101,
}

# 启发式函数，从图表读取的直线距离到 Bucharest
heuristics = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380,
    'Timisoara': 329, 'Lugoj': 244, 'Mehadia': 241,
    'Drobeta': 242, 'Craiova': 160, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Fagaras': 176, 'Pitesti': 98,
    'Bucharest': 0,
}

start_city = 'Arad'
goal_city = 'Bucharest'
path = a_star_search(graph, costs, heuristics, start_city, goal_city)
print("Path found using A*:", path)
