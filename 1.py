import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.blank_pos = self.find_blank()
        self.manhattan = self.calculate_manhattan()
        
    def find_blank(self):
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == 0:
                    return (i, j)
    
    def calculate_manhattan(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:
                    target_x = (value - 1) // 3
                    target_y = (value - 1) % 3
                    distance += abs(i - target_x) + abs(j - target_y)
        return distance
    
    def is_goal(self):
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    def neighbors(self):
        neighbors = []
        x, y = self.blank_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors
    
    def __lt__(self, other):
        return (self.moves + self.manhattan) < (other.moves + other.manhattan)

def a_star(start):
    open_set = []
    heapq.heappush(open_set, start)
    closed_set = set()
    while open_set:
        current = heapq.heappop(open_set)
        if current.is_goal():
            return current
        closed_set.add(tuple(map(tuple, current.board)))
        for neighbor in current.neighbors():
            if tuple(map(tuple, neighbor.board)) not in closed_set:
                heapq.heappush(open_set, neighbor)
    return None

def print_solution(solution):
    path = []
    while solution:
        path.append(solution.board)
        solution = solution.previous
    path.reverse()
    for step in path:
        for row in step:
            print(row)
        print()

# Example usage:
start_board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
start_state = PuzzleState(start_board)
solution = a_star(start_state)

if solution:
    print("Solution found!")
    print_solution(solution)
else:
    print("No solution exists.")
