def terminal_test(state):
    return state not in game_tree or not game_tree[state]


def utility(state):
    return utilities[state]


def successors(state):
    return game_tree[state] if state in game_tree else []


def alpha_beta_search(state, alpha, beta, is_max):
    if terminal_test(state):
        return utility(state)

    if is_max:
        value = float('-inf')
        for successor in successors(state):
            value = max(value, alpha_beta_search(successor, alpha, beta, False))
            if value >= beta:
                return value  # Beta 剪枝
            alpha = max(alpha, value)
    else:
        value = float('inf')
        for successor in successors(state):
            value = min(value, alpha_beta_search(successor, alpha, beta, True))
            if value <= alpha:
                return value  # Alpha 剪枝
            beta = min(beta, value)

    return value


def alpha_beta_decision(state):
    alpha = float('-inf')
    beta = float('inf')
    best_score = float('-inf')
    best_action = None

    for action in successors(state):
        value = alpha_beta_search(action, alpha, beta, False)
        if value > best_score:
            best_score = value
            best_action = action
        alpha = max(alpha, best_score)

    return best_action


# 以下是示例的游戏树和效用值
game_tree = {
    'A1': ['A11', 'A12', 'A13'],
    'A11': [], 'A12': [], 'A13': [],
    'A2': ['A21', 'A22', 'A23'],
    'A21': [], 'A22': [], 'A23': [],
    'A3': ['A31', 'A32', 'A33'],
    'A31': [], 'A32': [], 'A33': []
}

utilities = {
    'A11': 3, 'A12': 12, 'A13': 8,
    'A21': 2, 'A22': 4, 'A23': 6,
    'A31': 14, 'A32': 5, 'A33': 2
}

initial_state = 'A1'
best_move = alpha_beta_decision(initial_state)
print(f"Best move from {initial_state} according to Alpha-Beta: {best_move}")
