from collections import deque

# Function to display the solution path
def print_solution_path(path):
    for step in path:
        print(f"Jug1: {step[0]}, Jug2: {step[1]}")

# BFS algorithm to solve the Water Jug Problem
def water_jug_problem(capacity1, capacity2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))  # Initial state (both jugs are empty)
    parent = {(0, 0): None}  # Dictionary to store the parent of each state

    while queue:
        current_state = queue.popleft()
        x, y = current_state  # Current amount of water in jug1 and jug2

        if current_state in visited:
            continue

        visited.add(current_state)

        # Check if we have reached the target amount in either jug
        if x == target or y == target:
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = parent[current_state]
            path.reverse()
            print_solution_path(path)
            return

        # Possible actions
        possible_actions = [
            (capacity1, y),  # Fill jug1
            (x, capacity2),  # Fill jug2
            (0, y),  # Empty jug1
            (x, 0),  # Empty jug2
            (x - min(x, capacity2 - y), y + min(x, capacity2 - y)),  # Pour water from jug1 to jug2
            (x + min(y, capacity1 - x), y - min(y, capacity1 - x))  # Pour water from jug2 to jug1
        ]

        for next_state in possible_actions:
            if next_state not in visited:
                queue.append(next_state)
                parent[next_state] = current_state

    print("No solution found.")

# Example usage
if __name__ == "__main__":
    capacity1 = 4  # Capacity of jug1
    capacity2 = 3  # Capacity of jug2
    target = 2  # Target amount of water to measure

    water_jug_problem(capacity1, capacity2, target)
