def terminal_test(state):
    # 假设我们有一个终止检测函数
    return state in game_tree and not game_tree[state]

def utility(state):
    # 假设每个终止状态都有一个预定义的效用值
    return utilities[state]

def successors(state):
    # 生成给定状态的所有可能后继状态
    return game_tree[state] if state in game_tree else []

# 简化的游戏树和效用值（根据上传的图片）
game_tree = {
    'A1': ['A11', 'A12', 'A13'],
    'A11': [],  # 终止状态
    'A12': [],  # 终止状态
    'A13': [],  # 终止状态
    'A2': ['A21', 'A22', 'A23'],
    'A21': [],  # 终止状态
    'A22': [],  # 终止状态
    'A23': [],  # 终止状态
    'A3': ['A31', 'A32', 'A33'],
    'A31': [],  # 终止状态
    'A32': [],  # 终止状态
    'A33': []   # 终止状态
}

utilities = {
    'A11': 3, 'A12': 12, 'A13': 8,
    'A21': 2, 'A22': 4, 'A23': 6,
    'A31': 14, 'A32': 5, 'A33': 2
}

def minimax_decision(state):
    action_values = {action: minimax_value(action, False) for action in successors(state)}
    return max(action_values, key=action_values.get)

def minimax_value(state, is_max):
    if terminal_test(state):
        return utility(state)
    if is_max:
        return max(minimax_value(s, False) for s in successors(state))
    else:
        return min(minimax_value(s, True) for s in successors(state))

# 示例：从节点 'A1' 开始的 Minimax 决策
initial_state = 'A1'
best_move = minimax_decision(initial_state)
print(f"Best move from {initial_state} according to Minimax: {best_move}")
