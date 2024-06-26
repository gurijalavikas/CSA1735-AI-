from collections import deque
initial_state = (3, 3, 1)
goal_state = (0, 0, 0)  
def is_valid_state(state):
    missionaries_left, cannibals_left, _ = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left

    if missionaries_left < 0 or missionaries_right < 0 or cannibals_left < 0 or cannibals_right < 0:
        return False
    if (missionaries_left > 0 and missionaries_left < cannibals_left) or (missionaries_right > 0 and missionaries_right < cannibals_right):
        return False
    return True


def get_successors(state):
    successors = []
    missionaries_left, cannibals_left, boat_position = state
    if boat_position == 1:  
        new_states = [
            (missionaries_left - 2, cannibals_left, 0),
            (missionaries_left, cannibals_left - 2, 0),
            (missionaries_left - 1, cannibals_left - 1, 0),
            (missionaries_left - 1, cannibals_left, 0),
            (missionaries_left, cannibals_left - 1, 0)
        ]
    else: 
        new_states = [
            (missionaries_left + 2, cannibals_left, 1),
            (missionaries_left, cannibals_left + 2, 1),
            (missionaries_left + 1, cannibals_left + 1, 1),
            (missionaries_left + 1, cannibals_left, 1),
            (missionaries_left, cannibals_left + 1, 1)
        ]
    
    for new_state in new_states:
        if is_valid_state(new_state):
            successors.append(new_state)
    return successors
def missionaries_cannibals_bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path + [current_state]
        
        for successor in get_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [current_state]))
    
    return None


solution_path = missionaries_cannibals_bfs(initial_state, goal_state)


if solution_path:
    print("Solution path:")
    for step in solution_path:
        print(step)
else:
    print("No solution found.")
